# .NET 10.0.403 on Ubuntu 26.04; MCR index verified for linux/amd64 and linux/arm64 on 2026-11-06.
FROM mcr.microsoft.com/dotnet/sdk:10.0.403-resolute@sha256:2107242a0f56885d09f8a536ac300f6cb1a2b3f6d40605e5ff81bbd83ad91e3f AS dotnet-base
FROM dotnet-base AS sandbox

# toolchain-pin: argName=JAVA_VERSION
ARG JAVA_VERSION=25
# toolchain-pin: argName=MAVEN_VERSION
ARG MAVEN_VERSION=3.10.0
# toolchain-pin: argName=PYTHON_VERSION
ARG PYTHON_VERSION=3.15.2
# toolchain-pin: argName=PYTHON_BUILD_DATE
ARG PYTHON_BUILD_DATE=20261026
# toolchain-pin: argName=POWERSHELL_VERSION
ARG POWERSHELL_VERSION=7.6.9
# toolchain-pin: argName=GO_VERSION
ARG GO_VERSION=1.27.3
# toolchain-pin: argName=GOPLS_VERSION
ARG GOPLS_VERSION=v0.24.0
# toolchain-pin: argName=STATICCHECK_VERSION
ARG STATICCHECK_VERSION=v0.8.2
# toolchain-pin: argName=GOVULNCHECK_VERSION
ARG GOVULNCHECK_VERSION=v1.9.0
# toolchain-pin: argName=DELVE_VERSION
ARG DELVE_VERSION=v1.27.2
# toolchain-pin: argName=RUST_TOOLCHAIN
ARG RUST_TOOLCHAIN=1.99.1
# toolchain-pin: argName=RUSTUP_VERSION
ARG RUSTUP_VERSION=1.29.3
# toolchain-pin: argName=SWIFT_DOCKER_TAG
ARG SWIFT_DOCKER_TAG=6.4.2-resolute
# toolchain-pin: argName=NODE_MAJOR
ARG NODE_MAJOR=24
# toolchain-pin: argName=UV_VERSION
ARG UV_VERSION=0.13.7
# toolchain-pin: argName=OPENCODE_VERSION
ARG OPENCODE_VERSION=2.1.4
# toolchain-pin: argName=CODEX_VERSION
ARG CODEX_VERSION=0.164.0
# toolchain-pin: argName=CLAUDE_CODE_VERSION
ARG CLAUDE_CODE_VERSION=2.1.319
# toolchain-pin: argName=GEMINI_CLI_VERSION
ARG GEMINI_CLI_VERSION=0.65.0
# toolchain-pin: argName=ANTIGRAVITY_CLI_VERSION
ARG ANTIGRAVITY_CLI_VERSION=1.4.7
# toolchain-pin: argName=COPILOT_CLI_VERSION
ARG COPILOT_CLI_VERSION=1.0.106
# toolchain-pin: argName=SYFT_VERSION
ARG SYFT_VERSION=1.55.0
# toolchain-pin: argName=ACTIONLINT_VERSION
ARG ACTIONLINT_VERSION=1.7.12
# toolchain-pin: argName=DOTNET_COMPAT_SDK_VERSION
ARG DOTNET_COMPAT_SDK_VERSION=10.0.303

# toolchain-pin: argName=PANDOC_VERSION
ARG PANDOC_VERSION=3.12.1
# toolchain-pin: argName=LYCHEE_VERSION
ARG LYCHEE_VERSION=0.24.2
# toolchain-pin: argName=TYPST_VERSION
ARG TYPST_VERSION=0.15.1
# toolchain-pin: argName=TINYMIST_VERSION
ARG TINYMIST_VERSION=0.15.12

USER root
ENV POWERSHELL_TELEMETRY_OPTOUT=1
# Some Windows/Podman networks reject plain HTTP from containers. Keep the
# Ubuntu repositories and signature verification unchanged, using TLS transport.
RUN sed -i \
        -e 's|http://archive.ubuntu.com/ubuntu|https://archive.ubuntu.com/ubuntu|g' \
        -e 's|http://security.ubuntu.com/ubuntu|https://security.ubuntu.com/ubuntu|g' \
        -e 's|http://ports.ubuntu.com/ubuntu-ports|https://ports.ubuntu.com/ubuntu-ports|g' \
        /etc/apt/sources.list.d/ubuntu.sources \
    && apt-get -y update \
    && apt-get -y install --no-install-recommends \
        bubblewrap \
        build-essential \
        ca-certificates \
        curl \
        direnv \
        fd-find \
        fonts-dejavu-core \
        git \
        git-delta \
        gnupg \
        gnupg2 \
        jq \
        just \
        libcurl4-openssl-dev \
        libedit2 \
        libgcc-15-dev \
        libncurses5-dev \
        libsqlite3-0 \
        libssl-dev \
        libstdc++-15-dev \
        libxml2-dev \
        libz3-dev \
        pkg-config \
        poppler-utils \
        python3 \
        ripgrep \
        shellcheck \
        shfmt \
        tree \
        wget \
        xz-utils \
        yq \
    && mkdir -p /usr/share/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key -o /tmp/nodesource-repo.gpg.key \
    && gpg --dearmor --yes -o /usr/share/keyrings/nodesource.gpg /tmp/nodesource-repo.gpg.key \
    && chmod 0644 /usr/share/keyrings/nodesource.gpg \
    && rm /tmp/nodesource-repo.gpg.key \
    && arch="$(dpkg --print-architecture)" \
    && case "${arch}" in \
        amd64|arm64) ;; \
        *) echo "Unsupported NodeSource architecture: ${arch}" >&2; exit 1 ;; \
    esac \
    && printf 'Types: deb\nURIs: https://deb.nodesource.com/node_%s.x\nSuites: nodistro\nComponents: main\nArchitectures: %s\nSigned-By: /usr/share/keyrings/nodesource.gpg\n' "${NODE_MAJOR}" "${arch}" > /etc/apt/sources.list.d/nodesource.sources \
    && printf 'Package: nodejs\nPin: origin deb.nodesource.com\nPin-Priority: 600\n' > /etc/apt/preferences.d/nodejs \
    && apt-get -y update \
    && apt-get -y install --no-install-recommends nodejs \
    && ln -sf /usr/bin/fdfind /usr/local/bin/fd \
    && rm -rf /var/lib/apt/lists/*
# Build selector follows the large common APT layer so profiles share that cache.
# toolchain-pin: argName=ADE_MSL_PROFILE
ARG ADE_MSL_PROFILE=all
RUN case "${ADE_MSL_PROFILE}" in dotnet|java|go|rust|python|swift|all) ;; *) echo "Invalid ADE_MSL_PROFILE: ${ADE_MSL_PROFILE}" >&2; exit 2 ;; esac
ENV ADE_MSL_PROFILE=${ADE_MSL_PROFILE}
RUN if [ "${ADE_MSL_PROFILE}" = java ] || [ "${ADE_MSL_PROFILE}" = all ]; then \
      apt-get -y update \
      && apt-get -y install --no-install-recommends "openjdk-${JAVA_VERSION}-jdk-headless" \
      && rm -rf /var/lib/apt/lists/*; \
    fi
RUN if [ "${ADE_MSL_PROFILE}" = java ] || [ "${ADE_MSL_PROFILE}" = all ]; then \
    set -eux; \
    tmp_dir="$(mktemp -d)"; \
    archive="apache-maven-${MAVEN_VERSION}-bin.tar.gz"; \
    maven_major="${MAVEN_VERSION%%.*}"; \
    maven_sha512="908b1501bfb420bf7c8affb855534a9c407fd6099367bfb9f2f2dcb8e9799102bffb84518cde74c679bd76870247c6528683abdd620581bffa90f95d92d175aa"; \
    if ! curl -fsSL "https://dlcdn.apache.org/maven/maven-${maven_major}/${MAVEN_VERSION}/binaries/${archive}" -o "${tmp_dir}/${archive}"; then \
        curl -fsSL "https://archive.apache.org/dist/maven/maven-${maven_major}/${MAVEN_VERSION}/binaries/${archive}" -o "${tmp_dir}/${archive}"; \
    fi; \
    printf '%s  %s\n' "${maven_sha512}" "${tmp_dir}/${archive}" | sha512sum -c -; \
    tar -xzf "${tmp_dir}/${archive}" -C /opt; \
    ln -s "/opt/apache-maven-${MAVEN_VERSION}/bin/mvn" /usr/local/bin/mvn; \
    rm -rf "${tmp_dir}"; \
    mvn --version; \
    fi
RUN if [ "${ADE_MSL_PROFILE}" = python ] || [ "${ADE_MSL_PROFILE}" = all ]; then \
    set -eux; \
    apt-get -y update; \
    apt-get -y install --no-install-recommends libpython3-dev python3-venv; \
    rm -rf /var/lib/apt/lists/*; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) python_target="x86_64"; python_sha256="7b03163a980c607ba8194709d4a4086735a7a9c488cc475b098157306927b36b" ;; \
        arm64) python_target="aarch64"; python_sha256="0f23351c03b39beb880de668976074fcc3c082d9c3b03d0b43185632b2b270a0" ;; \
        *) echo "Unsupported Python architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="cpython-${PYTHON_VERSION}+${PYTHON_BUILD_DATE}-${python_target}-unknown-linux-gnu-install_only_stripped.tar.gz"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "https://github.com/astral-sh/python-build-standalone/releases/download/${PYTHON_BUILD_DATE}/${archive}" -o "${tmp_dir}/${archive}"; \
    printf '%s  %s\n' "${python_sha256}" "${tmp_dir}/${archive}" | sha256sum -c -; \
    mkdir -p /opt/cpython; \
    tar -xzf "${tmp_dir}/${archive}" --strip-components=1 -C /opt/cpython; \
    ln -s /opt/cpython/bin/python3 /usr/local/bin/python; \
    ln -s /opt/cpython/bin/python3 /usr/local/bin/python3; \
    rm -rf "${tmp_dir}"; \
    python3 -c 'import sys; assert sys.version.split()[0] == "'"${PYTHON_VERSION}"'", sys.version'; \
    fi
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) target="amd64"; checksum="d0c90410e90204c9ca83b8539fac5c7aed01fd537207e4585849f8abc5df20b8" ;; \
        arm64) target="arm64"; checksum="445d96fd08801fe636cab1158b4f017ee320ac3b7446328b4fe2f902117b19b9" ;; \
        *) echo "Unsupported pandoc architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="pandoc-${PANDOC_VERSION}-linux-${target}.tar.gz"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "https://github.com/jgm/pandoc/releases/download/${PANDOC_VERSION}/${archive}" -o "${tmp_dir}/${archive}"; \
    printf '%s  %s\n' "${checksum}" "${tmp_dir}/${archive}" | sha256sum -c -; \
    tar -xzf "${tmp_dir}/${archive}" -C "${tmp_dir}"; \
    install -m 0755 "${tmp_dir}/pandoc-${PANDOC_VERSION}/bin/pandoc" /usr/local/bin/pandoc; \
    rm -rf "${tmp_dir}"; \
    pandoc --version
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) target="x86_64"; checksum="1f4e0ef7f6554a6ed33dd7ac144fb2e1bbed98598e7af973042fc5cd43951c9a" ;; \
        arm64) target="aarch64"; checksum="91a7bd65685da41b90ccb9bc867a3d649a7818042dae04ff405e55a25bddee4c" ;; \
        *) echo "Unsupported lychee architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="lychee-${target}-unknown-linux-gnu.tar.gz"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "https://github.com/lycheeverse/lychee/releases/download/lychee-v${LYCHEE_VERSION}/${archive}" -o "${tmp_dir}/${archive}"; \
    printf '%s  %s\n' "${checksum}" "${tmp_dir}/${archive}" | sha256sum -c -; \
    tar -xzf "${tmp_dir}/${archive}" -C "${tmp_dir}"; \
    install -m 0755 "${tmp_dir}/lychee-${target}-unknown-linux-gnu/lychee" /usr/local/bin/lychee; \
    rm -rf "${tmp_dir}"; \
    lychee --version
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) target="x86_64"; checksum="a6d077d0a95eed5a2eba715b2dae06be954f624ccbf85758a03f389ded33118c" ;; \
        arm64) target="aarch64"; checksum="5aa8d74a3d906e60ea12a66ac2f37f8eef1b14cbad7182a745e393a10c23dcee" ;; \
        *) echo "Unsupported typst architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="typst-${target}-unknown-linux-musl.tar.xz"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "https://github.com/typst/typst/releases/download/v${TYPST_VERSION}/${archive}" -o "${tmp_dir}/${archive}"; \
    printf '%s  %s\n' "${checksum}" "${tmp_dir}/${archive}" | sha256sum -c -; \
    tar -xJf "${tmp_dir}/${archive}" -C "${tmp_dir}"; \
    install -m 0755 "${tmp_dir}/typst-${target}-unknown-linux-musl/typst" /usr/local/bin/typst; \
    rm -rf "${tmp_dir}"; \
    typst --version
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) target="x86_64"; checksum="95f98715f2bc3ecff528124dd691db074c15de1fe0ed2dfa8be43dda6dbbb967" ;; \
        arm64) target="aarch64"; checksum="d75cabad569b8fc7d24fa326a36ce0c2e3a287c5a4f66204c1fc302185225678" ;; \
        *) echo "Unsupported tinymist architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="tinymist-${target}-unknown-linux-gnu.tar.gz"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "https://github.com/Myriad-Dreamin/tinymist/releases/download/v${TINYMIST_VERSION}/${archive}" -o "${tmp_dir}/${archive}"; \
    printf '%s  %s\n' "${checksum}" "${tmp_dir}/${archive}" | sha256sum -c -; \
    tar -xzf "${tmp_dir}/${archive}" -C "${tmp_dir}"; \
    install -m 0755 "${tmp_dir}/tinymist-${target}-unknown-linux-gnu/tinymist" /usr/local/bin/tinymist; \
    rm -rf "${tmp_dir}"; \
    tinymist --version
# Install the checked package separately. Updating MCR's preinstalled tool in
# place can fail under rootless overlay storage while moving its old package.
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) ps_arch="x64"; ps_sha256="e14ad06e1192ccb221a6bfbc804476dabae792bb5c9c7ad62793e5ff058d826e" ;; \
        arm64) ps_arch="arm64"; ps_sha256="9d098cb700f518702a87bbc037dadb6a9d6b34489012431756fb2531503f436b" ;; \
        *) echo "Unsupported PowerShell architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    tmp_dir="$(mktemp -d)"; \
    package="PowerShell.Linux.${ps_arch}.${POWERSHELL_VERSION}.nupkg"; \
    curl -fsSL "https://powershellinfraartifacts-gkhedzdeaghdezhr.z01.azurefd.net/tool/${POWERSHELL_VERSION}/${package}" -o "${tmp_dir}/${package}"; \
    printf '%s  %s\n' "${ps_sha256}" "${tmp_dir}/${package}" | sha256sum -c -; \
    /usr/bin/dotnet tool install --tool-path /opt/powershell-pinned --add-source "${tmp_dir}" --version "${POWERSHELL_VERSION}" "PowerShell.Linux.${ps_arch}"; \
    ln -sfn /opt/powershell-pinned/pwsh /usr/bin/pwsh; \
    /usr/bin/dotnet nuget locals all --clear; \
    rm -rf "${tmp_dir}"
# The checked tool is the effective command; the MCR copy stays untouched.
RUN actual_version="$(pwsh -NoLogo -NoProfile -Command '$PSVersionTable.PSVersion.ToString()')" \
    && if [ "${actual_version}" != "${POWERSHELL_VERSION}" ]; then \
        echo "Expected PowerShell ${POWERSHELL_VERSION}, found ${actual_version}" >&2; \
        exit 1; \
    fi \
    && test "$(readlink -f /usr/bin/pwsh)" = /opt/powershell-pinned/pwsh
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) dotnet_rid="linux-x64"; dotnet_sha512="538df11ceb9d86bdda061bab6ede3d1f6d46bb9ba087ae905643f3d456afe982949d1b952bceb305a5d22d2d6e69cc0e5100216ffcc709aaa86e867f2d9cdf9a" ;; \
        arm64) dotnet_rid="linux-arm64"; dotnet_sha512="622e059198058ee5f92d7817bdd83885480a979628348f878201cb8dba52d168c1a324f9943a0e7a03ad547d85332aa82f16aced29da599ef02422b5378452de" ;; \
        *) echo "Unsupported .NET compatibility SDK architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="dotnet-sdk-${DOTNET_COMPAT_SDK_VERSION}-${dotnet_rid}.tar.gz"; \
    url="https://builds.dotnet.microsoft.com/dotnet/Sdk/${DOTNET_COMPAT_SDK_VERSION}/${archive}"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "${url}" -o "${tmp_dir}/${archive}"; \
    printf '%s  %s\n' "${dotnet_sha512}" "${tmp_dir}/${archive}" | sha512sum -c -; \
    tar -xzf "${tmp_dir}/${archive}" -C /usr/share/dotnet; \
    rm -rf "${tmp_dir}"; \
    /usr/bin/dotnet --list-sdks | grep -F "${DOTNET_COMPAT_SDK_VERSION} ["
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) actionlint_arch="amd64"; actionlint_sha256="8aca8db96f1b94770f1b0d72b6dddcb1ebb8123cb3712530b08cc387b349a3d8" ;; \
        arm64) actionlint_arch="arm64"; actionlint_sha256="325e971b6ba9bfa504672e29be93c24981eeb1c07576d730e9f7c8805afff0c6" ;; \
        *) echo "Unsupported actionlint architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="actionlint_${ACTIONLINT_VERSION}_linux_${actionlint_arch}.tar.gz"; \
    base_url="https://github.com/rhysd/actionlint/releases/download/v${ACTIONLINT_VERSION}"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "${base_url}/${archive}" -o "${tmp_dir}/${archive}"; \
    printf '%s  %s\n' "${actionlint_sha256}" "${tmp_dir}/${archive}" | sha256sum -c -; \
    tar -xzf "${tmp_dir}/${archive}" -C "${tmp_dir}" actionlint; \
    install -m 0755 "${tmp_dir}/actionlint" /usr/local/bin/actionlint; \
    rm -rf "${tmp_dir}"; \
    actionlint -version
RUN if [ "${ADE_MSL_PROFILE}" = swift ] || [ "${ADE_MSL_PROFILE}" = all ]; then \
    set -eux; \
    case "${SWIFT_DOCKER_TAG}" in \
        *-resolute) ;; \
        *) echo "Unsupported Swift Docker tag for Ubuntu 26.04 base image: ${SWIFT_DOCKER_TAG}" >&2; exit 1 ;; \
    esac; \
    swift_base_version="${SWIFT_DOCKER_TAG%%-*}"; \
    case "${swift_base_version}" in \
        [0-9]*.[0-9]*.[0-9]*) ;; \
        *) echo "Unsupported Swift version in SWIFT_DOCKER_TAG: ${SWIFT_DOCKER_TAG}" >&2; exit 1 ;; \
    esac; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) os_arch_suffix="" ;; \
        arm64) os_arch_suffix="-aarch64" ;; \
        *) echo "Unsupported Swift architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    swift_signing_key="52BB7E3DE28A71BE22EC05FFEF80A866B47A981F"; \
    swift_signing_keys_url="https://www.swift.org/keys/release-key-swift-6.x.asc"; \
    swift_platform="ubuntu26.04"; \
    swift_branch="swift-${swift_base_version}-release"; \
    swift_version="swift-${swift_base_version}-RELEASE"; \
    swift_webdir="https://download.swift.org/${swift_branch}/$(printf '%s' "${swift_platform}" | tr -d .)${os_arch_suffix}"; \
    swift_bin_url="${swift_webdir}/${swift_version}/${swift_version}-${swift_platform}${os_arch_suffix}.tar.gz"; \
    tmp_dir="$(mktemp -d)"; \
    export GNUPGHOME="${tmp_dir}/gnupg"; \
    install -d -m 0700 "${GNUPGHOME}"; \
    curl -fsSL "${swift_bin_url}" -o "${tmp_dir}/swift.tar.gz"; \
    curl -fsSL "${swift_bin_url}.sig" -o "${tmp_dir}/swift.tar.gz.sig"; \
    curl --compressed -fsSL "${swift_signing_keys_url}" -o "${tmp_dir}/swift-keys.asc"; \
    gpg --batch --quiet --import "${tmp_dir}/swift-keys.asc"; \
    gpg --batch --list-keys "${swift_signing_key}" >/dev/null; \
    gpg --batch --assert-signer "${swift_signing_key}" --verify "${tmp_dir}/swift.tar.gz.sig" "${tmp_dir}/swift.tar.gz"; \
    tar -xzf "${tmp_dir}/swift.tar.gz" --directory / --strip-components=1; \
    chmod -R o+r /usr/lib/swift; \
    rm -rf "${tmp_dir}"; \
    swift --version; \
    swiftc --version; \
    command -v sourcekit-lsp; \
    fi
RUN if [ "${ADE_MSL_PROFILE}" = go ] || [ "${ADE_MSL_PROFILE}" = all ]; then \
    set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) go_arch="amd64"; go_sha256="65efbc80fdc1fa2cd2631cad5b481777a68e8725f34e89f50fc6ac714e379b40" ;; \
        arm64) go_arch="arm64"; go_sha256="a06e99309dbcbdca1a8ccd2282c3ee146e55930886e26b4f1193269587165f49" ;; \
        *) echo "Unsupported Go architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    wget "https://go.dev/dl/go${GO_VERSION}.linux-${go_arch}.tar.gz" -O /tmp/go.tgz; \
    printf '%s  %s\n' "${go_sha256}" /tmp/go.tgz | sha256sum -c -; \
    rm -rf /usr/local/go; \
    tar -C /usr/local -xzf /tmp/go.tgz; \
    rm /tmp/go.tgz; \
    fi
RUN printf '%s\n' 'export PATH="/usr/local/go/bin:/home/adedev/go/bin:/home/adedev/.cargo/bin:${PATH}"' \
    > /etc/profile.d/ade-toolchains.sh
RUN npm i -g \
        "@opencode/cli@${OPENCODE_VERSION}" \
        "@openai/codex@${CODEX_VERSION}" \
        "@anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}" \
        "@google/gemini-cli@${GEMINI_CLI_VERSION}" \
        "@github/copilot@${COPILOT_CLI_VERSION}" \
    && ln -sf "$(npm root -g)/@openai/codex/bin/codex.js" /usr/local/bin/codex
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) syft_arch="amd64"; syft_sha256="bb65249542db5fedeeb4d3f9b018b75e7264dbfbbb10486f044581a92f90490d" ;; \
        arm64) syft_arch="arm64"; syft_sha256="929bd163db2d7cd2255d3bcb8967208079813d7b46b0c952f7b794d8e2c7d304" ;; \
        *) echo "Unsupported Syft architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="syft_${SYFT_VERSION}_linux_${syft_arch}.tar.gz"; \
    base_url="https://github.com/anchore/syft/releases/download/v${SYFT_VERSION}"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "${base_url}/${archive}" -o "${tmp_dir}/${archive}"; \
    printf '%s  %s\n' "${syft_sha256}" "${tmp_dir}/${archive}" | sha256sum -c -; \
    tar -xzf "${tmp_dir}/${archive}" -C /usr/local/bin syft; \
    chmod 0755 /usr/local/bin/syft; \
    rm -rf "${tmp_dir}"
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) uv_target="x86_64-unknown-linux-gnu"; uv_sha256="c5221ff41b7892bfc223543883600125f6a47fe845093e0f5bdff4f359196d83" ;; \
        arm64) uv_target="aarch64-unknown-linux-gnu"; uv_sha256="71279f8d3c67241e807b9d8db872d1bf541579fb9f08b7d1eb1682196d1e57dc" ;; \
        *) echo "Unsupported uv architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    uv_archive="uv-${uv_target}.tar.gz"; \
    uv_base_url="https://github.com/astral-sh/uv/releases/download/${UV_VERSION}"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "${uv_base_url}/${uv_archive}" -o "${tmp_dir}/${uv_archive}"; \
    printf '%s  %s\n' "${uv_sha256}" "${tmp_dir}/${uv_archive}" | sha256sum -c -; \
    tar -xzf "${tmp_dir}/${uv_archive}" -C "${tmp_dir}"; \
    install -m 0755 "${tmp_dir}/uv-${uv_target}/uv" /usr/local/bin/uv; \
    install -m 0755 "${tmp_dir}/uv-${uv_target}/uvx" /usr/local/bin/uvx; \
    rm -rf "${tmp_dir}"
COPY ./dotnet/dotnet-wrapper.sh /usr/local/bin/dotnet
RUN sed -i 's/\r$//' /usr/local/bin/dotnet \
    && chmod 0755 /usr/local/bin/dotnet
COPY ./spec-kit/patch-specify-cli.py /usr/local/bin/patch-specify-cli.py
RUN chmod 0644 /usr/local/bin/patch-specify-cli.py
RUN mkdir -p /etc/codex
COPY ./codex/config.toml /etc/codex/config.toml
COPY ./codex/requirements.toml /etc/codex/requirements.toml
RUN chmod 0644 /etc/codex/config.toml /etc/codex/requirements.toml
COPY ./gemini/system-settings.json /etc/gemini-cli/settings.json
RUN chmod 0644 /etc/gemini-cli/settings.json

RUN useradd -m adedev
RUN mkdir -p /dotnet-build && chown adedev:adedev /dotnet-build
USER adedev
ENV PATH="/usr/local/go/bin:/home/adedev/go/bin:/home/adedev/.cargo/bin:/home/adedev/.local/bin:${PATH}"
ENV CODEX_HOME="/home/adedev/.codex" \
    CLAUDE_CONFIG_DIR="/home/adedev/.claude" \
    GEMINI_CLI_HOME="/home/adedev/.gemini-home" \
    COPILOT_HOME="/home/adedev/.copilot" \
    COPILOT_AUTO_UPDATE="false" \
    AGY_CLI_DISABLE_AUTO_UPDATE="true" \
    DISABLE_AUTOUPDATER="1" \
    ADE_AGENT_PROMPT_TARGET="local"
WORKDIR /home/adedev
RUN if [ "${ADE_MSL_PROFILE}" = go ] || [ "${ADE_MSL_PROFILE}" = all ]; then \
      go install "golang.org/x/tools/gopls@${GOPLS_VERSION}" \
      && go install "honnef.co/go/tools/cmd/staticcheck@${STATICCHECK_VERSION}" \
      && go install "golang.org/x/vuln/cmd/govulncheck@${GOVULNCHECK_VERSION}" \
      && go install "github.com/go-delve/delve/cmd/dlv@${DELVE_VERSION}"; \
    fi
RUN if [ "${ADE_MSL_PROFILE}" = rust ] || [ "${ADE_MSL_PROFILE}" = all ]; then \
    set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) rust_host="x86_64-unknown-linux-gnu" ;; \
        arm64) rust_host="aarch64-unknown-linux-gnu" ;; \
        *) echo "Unsupported rustup architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    rustup_base_url="https://static.rust-lang.org/rustup/archive/${RUSTUP_VERSION}/${rust_host}"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "${rustup_base_url}/rustup-init" -o "${tmp_dir}/rustup-init"; \
    curl -fsSL "${rustup_base_url}/rustup-init.sha256" -o "${tmp_dir}/rustup-init.sha256"; \
    (cd "${tmp_dir}" && sha256sum -c rustup-init.sha256); \
    chmod 0755 "${tmp_dir}/rustup-init"; \
    "${tmp_dir}/rustup-init" -y --no-modify-path --profile minimal --default-host "${rust_host}" --default-toolchain "${RUST_TOOLCHAIN}"; \
    rm -rf "${tmp_dir}"; \
    rustup component add rustfmt clippy rust-analyzer rust-src; \
    fi
# Spec Kit v1.2.3: pin the peeled release commit, not a movable tag.
# Keep the existing bind-mount patch and reject unexpected package metadata.
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@5ea8b1cf0a38699340a38e00d02770308997d8c0 \
    && python3 /usr/local/bin/patch-specify-cli.py \
    && /home/adedev/.local/share/uv/tools/specify-cli/bin/python -c \
        'from importlib.metadata import version; actual = version("specify-cli"); assert actual == "1.2.3", actual'
RUN mkdir -p \
      /home/adedev/.local/share/opencode \
      /home/adedev/.codex \
      /home/adedev/.claude \
      /home/adedev/.gemini-home \
      /home/adedev/.copilot
COPY --chown=adedev:adedev ./opencode.jsonc /home/adedev/.config/opencode/opencode.jsonc
USER root
COPY ./scripts/codex-bwrap-wrapper.sh /usr/local/libexec/codex-bwrap-wrapper
RUN mkdir -p /usr/libexec \
    && install -d -m 0555 /usr/libexec/codex-empty-readonly \
    && mv /usr/bin/bwrap /usr/libexec/codex-bwrap.real \
    && install -m 0755 /usr/local/libexec/codex-bwrap-wrapper /usr/bin/bwrap \
    && mkdir -p /home/adedev/codex-workspace/.git \
        /home/adedev/codex-workspace/.agents \
        /home/adedev/codex-workspace/.codex \
    && chown root:root /home/adedev/codex-workspace \
        /home/adedev/codex-workspace/.git \
        /home/adedev/codex-workspace/.agents \
        /home/adedev/codex-workspace/.codex \
    && chmod 1777 /home/adedev/codex-workspace \
    && chmod 0755 /home/adedev/codex-workspace/.git \
        /home/adedev/codex-workspace/.agents \
        /home/adedev/codex-workspace/.codex
COPY ./scripts/audit-export.sh /usr/local/bin/audit-export
COPY ./scripts/lib/audit_retention.py /usr/local/bin/audit-retention
COPY ./scripts/container-entrypoint.sh /usr/local/bin/ade-entrypoint
COPY ./scripts/install-home-baseline-reference.sh /usr/local/bin/install-home-baseline-reference
COPY ./scripts/sync-home-baseline-runtime.sh /usr/local/bin/sync-home-baseline-runtime
COPY ./scripts/agent-prompt.sh /usr/local/bin/agent-prompt
COPY ./scripts/agent-prompt.ps1 /usr/local/bin/agent-prompt.ps1
COPY ./scripts/opencode-web.sh /usr/local/bin/opencode-web
COPY ./scripts/opencode-tui.sh /usr/local/bin/opencode-tui
COPY ./scripts/opencode-tui-mini.sh /usr/local/bin/opencode-tui-mini
COPY ./scripts/healthcheck-opencode-web.py /usr/local/bin/healthcheck-opencode-web
COPY ./scripts/test-opencode-local-web.py /usr/local/bin/test-opencode-local-web
COPY ./home-baseline.lock.json /usr/local/share/absdd-image-sandbox/home-baseline.lock.json
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) agy_arch="x64"; agy_sha256="67fd4e70be739b1f8b18f90b511da8cd2a7aef24e888e5837402e025bf7fdbfc" ;; \
        arm64) agy_arch="arm64"; agy_sha256="b273c791b7647f680598fa1dbdf9c8086bdc42374b2276fa70e900bf8120e1d5" ;; \
        *) echo "Unsupported Antigravity CLI architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="agy_cli_linux_${agy_arch}.tar.gz"; \
    base_url="https://github.com/google-antigravity/antigravity-cli/releases/download/${ANTIGRAVITY_CLI_VERSION}"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "${base_url}/${archive}" -o "${tmp_dir}/${archive}"; \
    printf '%s  %s\n' "${agy_sha256}" "${tmp_dir}/${archive}" | sha256sum -c -; \
    tar -xzf "${tmp_dir}/${archive}" -C "${tmp_dir}" antigravity; \
    install -m 0755 "${tmp_dir}/antigravity" /usr/local/bin/agy; \
    rm -rf "${tmp_dir}"
RUN sed -i 's/\r$//' /usr/local/bin/audit-export /usr/local/bin/audit-retention /usr/local/bin/ade-entrypoint \
        /usr/local/bin/install-home-baseline-reference /usr/local/bin/sync-home-baseline-runtime \
        /usr/local/bin/agent-prompt /usr/local/bin/agent-prompt.ps1 \
        /usr/local/bin/opencode-web /usr/local/bin/opencode-tui /usr/local/bin/opencode-tui-mini /usr/local/bin/healthcheck-opencode-web /usr/local/bin/test-opencode-local-web \
    && chmod 0755 /usr/local/bin/audit-export /usr/local/bin/audit-retention /usr/local/bin/ade-entrypoint \
        /usr/local/bin/install-home-baseline-reference /usr/local/bin/sync-home-baseline-runtime \
        /usr/local/bin/agent-prompt /usr/local/bin/agent-prompt.ps1 \
        /usr/local/bin/opencode-web /usr/local/bin/opencode-tui /usr/local/bin/opencode-tui-mini /usr/local/bin/healthcheck-opencode-web /usr/local/bin/test-opencode-local-web \
    && install-home-baseline-reference \
        /usr/local/share/absdd-image-sandbox/home-baseline.lock.json \
        /opt/home-baseline \
    && ln -s /opt/home-baseline /home/adedev/home-baseline-source \
    && ln -s /opt/home-baseline /home/adedev/home-baseline-tmp \
    && chown -h adedev:adedev /home/adedev/home-baseline-source \
        /home/adedev/home-baseline-tmp
# npm now blocks unnamed install hooks. Finalize only these native-agent hooks;
# do not persist an npm allow-scripts setting or grant agent permissions.
RUN apt-get -y update \
    && apt-get -y install --no-install-recommends libsecret-1-0 \
    && rm -rf /var/lib/apt/lists/* \
    && PYTHON=/usr/bin/python3 npm rebuild --global \
        --allow-scripts=@opencode/cli,@anthropic-ai/claude-code,@github/keytar,node-pty \
        @opencode/cli @anthropic-ai/claude-code @github/keytar node-pty \
    && opencode --version \
    && claude --version \
    && node -e 'for (const p of process.argv.slice(1)) require(p)' \
        "$(npm root -g)/@google/gemini-cli/node_modules/@github/keytar" \
        "$(npm root -g)/@google/gemini-cli/node_modules/@lydell/node-pty" \
        "$(npm root -g)/@google/gemini-cli/node_modules/node-pty"
# toolchain-pin: argName=NPM_VERSION
ARG NPM_VERSION=12.2.2
RUN npm install --global "npm@${NPM_VERSION}" \
    && npm --version
# The compatibility SDK archive must not downgrade the base host or retain old runtimes.
COPY --from=dotnet-base /usr/share/dotnet/dotnet /usr/share/dotnet/dotnet
RUN set -eux; \
    for root in /usr/share/dotnet/shared/Microsoft.NETCore.App /usr/share/dotnet/shared/Microsoft.AspNetCore.App /usr/share/dotnet/host/fxr; do \
        newest="$(find "${root}" -mindepth 1 -maxdepth 1 -type d -name '10.*' -exec basename {} \; | sort -V | tail -n 1)"; \
        test -n "${newest}"; \
        for path in "${root}"/10.*; do \
            if [ -d "${path}" ] && [ "${path##*/}" != "${newest}" ]; then \
                rm -rf "${path}"; \
            fi; \
        done; \
    done; \
    /usr/bin/dotnet --list-runtimes
RUN install -d -m 0755 /usr/local/share/ade \
    && printf '{"profile":"%s"}\n' "${ADE_MSL_PROFILE}" > /usr/local/share/ade/msl-profile.json
LABEL org.absdd-image-sandbox.msl-profile="${ADE_MSL_PROFILE}"
USER adedev

ENTRYPOINT ["/usr/local/bin/ade-entrypoint"]
HEALTHCHECK --interval=10s --timeout=50s --start-period=45s --retries=3 CMD ["/usr/local/bin/healthcheck-opencode-web"]
CMD ["/usr/local/bin/opencode-web"]

# Buildah visits preceding named stages when targeting ade-all. Keep these
# aliases side-effect-free; the validated ARG sets contents, manifest and label.
FROM sandbox AS ade-dotnet

FROM sandbox AS ade-java

FROM sandbox AS ade-go

FROM sandbox AS ade-rust

FROM sandbox AS ade-python

FROM sandbox AS ade-swift

FROM sandbox AS ade-all

# An unqualified direct build preserves the original six-toolchain image.
FROM ade-all AS sandbox-default
