# Tag 10.0 observed on 2026-10-25: SDK 10.0.402, native AMD64/ARM64 manifest.
FROM mcr.microsoft.com/dotnet/sdk:10.0@sha256:747cbade5bfd918a175ac32f8f1d931edec2c7d0d5397a3de72eaef1ac1f66d2 AS dotnet-base
FROM dotnet-base AS sandbox

# renovate: datasource=java-version depName=java packageName=java-jdk versioning=semver-coerced argName=JAVA_VERSION
ARG JAVA_VERSION=25
# renovate: datasource=maven depName=org.apache.maven:apache-maven versioning=maven argName=MAVEN_VERSION
ARG MAVEN_VERSION=3.10.0
# renovate: datasource=python-version depName=python versioning=pep440 argName=PYTHON_VERSION
ARG PYTHON_VERSION=3.15.1
# renovate: datasource=github-releases depName=astral-sh/python-build-standalone versioning=loose argName=PYTHON_BUILD_DATE
ARG PYTHON_BUILD_DATE=20261021
# renovate: datasource=github-releases depName=PowerShell/PowerShell versioning=semver argName=POWERSHELL_VERSION
ARG POWERSHELL_VERSION=7.6.8
# renovate: datasource=golang-version depName=go versioning=semver argName=GO_VERSION
ARG GO_VERSION=1.27.3
# renovate: datasource=go depName=golang.org/x/tools/gopls versioning=semver argName=GOPLS_VERSION
ARG GOPLS_VERSION=v0.24.0
# renovate: datasource=go depName=honnef.co/go/tools versioning=semver argName=STATICCHECK_VERSION
ARG STATICCHECK_VERSION=v0.8.2
# renovate: datasource=go depName=golang.org/x/vuln versioning=semver argName=GOVULNCHECK_VERSION
ARG GOVULNCHECK_VERSION=v1.9.0
# renovate: datasource=go depName=github.com/go-delve/delve versioning=semver argName=DELVE_VERSION
ARG DELVE_VERSION=v1.27.2
# renovate: datasource=rust-version depName=rust versioning=rust-release-channel argName=RUST_TOOLCHAIN
ARG RUST_TOOLCHAIN=1.99.1
# renovate: datasource=github-releases depName=rust-lang/rustup versioning=semver argName=RUSTUP_VERSION
ARG RUSTUP_VERSION=1.29.2
# renovate: datasource=docker depName=swift versioning=docker argName=SWIFT_DOCKER_TAG
ARG SWIFT_DOCKER_TAG=6.4.1-noble
# renovate: datasource=node-version depName=node versioning=node argName=NODE_MAJOR
ARG NODE_MAJOR=24
# renovate: datasource=github-releases depName=astral-sh/uv versioning=semver argName=UV_VERSION
ARG UV_VERSION=0.13.5
# renovate: datasource=npm depName=@opencode/cli versioning=npm argName=OPENCODE_VERSION
ARG OPENCODE_VERSION=2.1.4
# renovate: datasource=npm depName=@openai/codex versioning=npm argName=CODEX_VERSION
ARG CODEX_VERSION=0.164.0
# renovate: datasource=npm depName=@anthropic-ai/claude-code versioning=npm argName=CLAUDE_CODE_VERSION
ARG CLAUDE_CODE_VERSION=2.1.310
# renovate: datasource=npm depName=@google/gemini-cli versioning=npm argName=GEMINI_CLI_VERSION
ARG GEMINI_CLI_VERSION=0.65.0
# renovate: datasource=github-releases depName=google-antigravity/antigravity-cli versioning=semver argName=ANTIGRAVITY_CLI_VERSION
ARG ANTIGRAVITY_CLI_VERSION=1.4.7
# renovate: datasource=npm depName=@github/copilot versioning=npm argName=COPILOT_CLI_VERSION
ARG COPILOT_CLI_VERSION=1.0.103
# renovate: datasource=github-releases depName=anchore/syft versioning=semver argName=SYFT_VERSION
ARG SYFT_VERSION=1.55.0
# renovate: datasource=github-releases depName=rhysd/actionlint versioning=semver argName=ACTIONLINT_VERSION
ARG ACTIONLINT_VERSION=1.7.12
# renovate: datasource=dotnet-version depName=dotnet-sdk versioning=semver argName=DOTNET_COMPAT_SDK_VERSION
ARG DOTNET_COMPAT_SDK_VERSION=10.0.303

# renovate: datasource=github-releases depName=jgm/pandoc versioning=semver-coerced argName=PANDOC_VERSION
ARG PANDOC_VERSION=3.12.1
# renovate: datasource=github-releases depName=lycheeverse/lychee versioning=semver argName=LYCHEE_VERSION
ARG LYCHEE_VERSION=0.24.2
# renovate: datasource=github-releases depName=typst/typst versioning=semver argName=TYPST_VERSION
ARG TYPST_VERSION=0.15.1
# renovate: datasource=github-releases depName=Myriad-Dreamin/tinymist versioning=semver argName=TINYMIST_VERSION
ARG TINYMIST_VERSION=0.15.10

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
        libgcc-13-dev \
        libncurses-dev \
        libpython3-dev \
        libsqlite3-0 \
        libssl-dev \
        libstdc++-13-dev \
        libxml2-dev \
        libz3-dev \
        openjdk-${JAVA_VERSION}-jdk-headless \
        pkg-config \
        poppler-utils \
        python-is-python3 \
        python3 \
        python3-venv \
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
RUN set -eux; \
    tmp_dir="$(mktemp -d)"; \
    archive="apache-maven-${MAVEN_VERSION}-bin.tar.gz"; \
    maven_sha512="908b1501bfb420bf7c8affb855534a9c407fd6099367bfb9f2f2dcb8e9799102bffb84518cde74c679bd76870247c6528683abdd620581bffa90f95d92d175aa"; \
    if ! curl -fsSL "https://dlcdn.apache.org/maven/maven-3/${MAVEN_VERSION}/binaries/${archive}" -o "${tmp_dir}/${archive}"; then \
        curl -fsSL "https://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/${archive}" -o "${tmp_dir}/${archive}"; \
    fi; \
    printf '%s  %s\n' "${maven_sha512}" "${tmp_dir}/${archive}" | sha512sum -c -; \
    tar -xzf "${tmp_dir}/${archive}" -C /opt; \
    ln -s "/opt/apache-maven-${MAVEN_VERSION}/bin/mvn" /usr/local/bin/mvn; \
    rm -rf "${tmp_dir}"; \
    mvn --version
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) python_target="x86_64"; python_sha256="01d901e09ca673c99a6c9bd9ec2cfbd58dbe8813d07514c36cb73cfd20b18bd8" ;; \
        arm64) python_target="aarch64"; python_sha256="6efe65c43ae0bdebebeab4607f91a0053dd36d5e51cfd69a791d544e9b122be7" ;; \
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
    python3 -c 'import sys; assert sys.version.split()[0] == "'"${PYTHON_VERSION}"'", sys.version'
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
        amd64) target="x86_64"; checksum="10df33ec0b6cb380b1354b55bd8a32fdc2f00fec281b7dc0a41086bd0038e0fc" ;; \
        arm64) target="aarch64"; checksum="0a545957d894cec8a4ca9010d05a7fa27beb1e356c2b221b7f7f704538ff0bb0" ;; \
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
        amd64) ps_arch="x64"; ps_sha256="caeeff1d808dd54a9fde06976e17c5c92061989dc5fbe21e13bd5690883e4eb1" ;; \
        arm64) ps_arch="arm64"; ps_sha256="6cddb58e698125156c725d57b5942f7e0468cd75e8f7b78b133641ede1a28a8e" ;; \
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
RUN set -eux; \
    case "${SWIFT_DOCKER_TAG}" in \
        *-noble) ;; \
        *) echo "Unsupported Swift Docker tag for Ubuntu 24.04 base image: ${SWIFT_DOCKER_TAG}" >&2; exit 1 ;; \
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
    swift_platform="ubuntu24.04"; \
    swift_branch="swift-${swift_base_version}-release"; \
    swift_version="swift-${swift_base_version}-RELEASE"; \
    swift_webdir="https://download.swift.org/${swift_branch}/$(printf '%s' "${swift_platform}" | tr -d .)${os_arch_suffix}"; \
    swift_bin_url="${swift_webdir}/${swift_version}/${swift_version}-${swift_platform}${os_arch_suffix}.tar.gz"; \
    tmp_dir="$(mktemp -d)"; \
    export GNUPGHOME="${tmp_dir}/gnupg"; \
    mkdir -p "${GNUPGHOME}"; \
    curl -fsSL "${swift_bin_url}" -o "${tmp_dir}/swift.tar.gz"; \
    curl -fsSL "${swift_bin_url}.sig" -o "${tmp_dir}/swift.tar.gz.sig"; \
    curl --compressed -fsSL "${swift_signing_keys_url}" -o "${tmp_dir}/swift-keys.asc"; \
    gpg --batch --quiet --import "${tmp_dir}/swift-keys.asc"; \
    gpg --batch --list-keys "${swift_signing_key}" >/dev/null; \
    gpg --batch --assert-signer "${swift_signing_key}" --verify "${tmp_dir}/swift.tar.gz.sig" "${tmp_dir}/swift.tar.gz"; \
    tar -xzf "${tmp_dir}/swift.tar.gz" --directory / --strip-components=1; \
    chmod -R o+r /usr/lib/swift; \
    rm -rf "${tmp_dir}"
RUN swift --version \
    && swiftc --version \
    && command -v sourcekit-lsp
RUN set -eux; \
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
    rm /tmp/go.tgz
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
        amd64) uv_target="x86_64-unknown-linux-gnu"; uv_sha256="f68d291c75783122dad58ab77def0e13f3233f358731db5d6d7e8715603b928f" ;; \
        arm64) uv_target="aarch64-unknown-linux-gnu"; uv_sha256="4bb69cf95ed13f23713bb7bc09f241896ea0c75b7c557e615a20604b82f9c403" ;; \
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
RUN go install "golang.org/x/tools/gopls@${GOPLS_VERSION}" \
    && go install "honnef.co/go/tools/cmd/staticcheck@${STATICCHECK_VERSION}" \
    && go install "golang.org/x/vuln/cmd/govulncheck@${GOVULNCHECK_VERSION}" \
    && go install "github.com/go-delve/delve/cmd/dlv@${DELVE_VERSION}"
RUN set -eux; \
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
    rustup component add rustfmt clippy rust-analyzer rust-src
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
    && chmod 0755 /usr/local/bin/audit-export /usr/local/bin/audit-retention /usr/local/bin/ade-entrypoint \
        /usr/local/bin/install-home-baseline-reference /usr/local/bin/sync-home-baseline-runtime \
        /usr/local/bin/agent-prompt /usr/local/bin/agent-prompt.ps1 \
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
# renovate: datasource=npm depName=npm versioning=npm argName=NPM_VERSION
ARG NPM_VERSION=12.2.1
RUN npm install --global "npm@${NPM_VERSION}" \
    && npm --version
# The compatibility SDK archive must not downgrade the base host or retain old runtimes.
COPY --from=dotnet-base /usr/share/dotnet/dotnet /usr/share/dotnet/dotnet
RUN set -eux; \
    for root in /usr/share/dotnet/shared/Microsoft.NETCore.App /usr/share/dotnet/shared/Microsoft.AspNetCore.App /usr/share/dotnet/host/fxr; do \
        for path in "${root}/${DOTNET_VERSION%.*}".*; do \
            if [ -d "${path}" ] && [ "${path##*/}" != "${DOTNET_VERSION}" ]; then \
                rm -rf "${path}"; \
            fi; \
        done; \
    done; \
    /usr/bin/dotnet --list-runtimes
USER adedev

ENTRYPOINT ["/usr/local/bin/ade-entrypoint"]
CMD ["/bin/bash", "-c", "while :; do sleep 1; done;"]
