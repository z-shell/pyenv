<h1 align="center">
  <a href="https://github.com/z-shell/zi">
    <p><img src="https://github.com/z-shell/zi/raw/main/docs/images/logo.svg" alt="Logo" width="60px" height="60px" /></a>
  ❮ ZI ❯ Package - Pyenv </p>
</h1>
<h3 align="center">
<table>
    <tr>
        <td><b>Package source:</b></td>
        <td>Source Tarball</td>
        <td>Binary</td>
        <td>Git</td>
        <td>Node</td>
        <td>Gem</td>
    </tr>
    <tr>
        <td><b>Status:</b></td>
        <td>✔️ (default)</td>
        <td>❌</td>
        <td>✔️</td>
        <td>❌</td>
        <td>❌</td>
    </tr>
</table></h3><hr />

### Available `pack''` invocations

```shell
# Download the tarball with the default ice list
zi pack for pyenv
```

```shell
# Download the tarball with the bin-gem-node annex-utilizing ice list
zi pack"bgn" for pyenv
```

```shell
# Download with the bin-gem-node annex-utilizing ice list FROM GIT REPOSITORY
zi pack"bgn" git for pyenv
```

### Default profile

`zi pack for pyenv` loads the native `bin/pyenv` program and initializes Zsh.
It preserves an existing `PYENV_ROOT`, defaulting to `$HOME/.pyenv`, so installed
interpreters live separately from the package checkout. Set your root before
loading the package. No interpreter is installed or selected automatically.

Initialization uses `pyenv init - zsh` at load time and refreshes command lookup.
This avoids caching initialization for a different root. Pyenv intentionally
places its shims first in PATH; project and shell selections then control Python
resolution. Git updates refresh the package without replacing your root.

### `Bin-Gem-Node` profile

`zi pack"bgn" for pyenv` retains the optional forwarder under `$ZPFX/bin` and
requires the [bin-gem-node annex](https://github.com/z-shell/z-a-bin-gem-node).
It uses the same root-preserving initialization as the default profile.

Existing users whose interpreters reside inside the old package checkout should
set `PYENV_ROOT` to that directory before loading, or migrate those installations
separately. The package does not delete or move interpreter installations.

---

> This repository compatible with [ZI](https://github.com/z-shell/zi)

The [pyenv/pyenv](https://github.com/pyenv/pyenv) zsh package. Zi's package support reads its `package.json` to automatically:

- get the plugin's Git repository OR release-package URL,
- get the list of the recommended ices for the plugin,
  - there can be multiple lists of ices,
  - the ice lists are stored in _profiles_; there's at least one profile, _default_,
  - the ices can be selectively overridden.
