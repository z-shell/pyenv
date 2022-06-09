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

Provides the `pyenv` version manager by extending `$PATH` to make it point into the `bin` subdirectory of the plugin.

The ZI command executed will be equivalent to:

```shell
zi lucid as'command' pick'bin/pyenv' atinit'export PYENV_ROOT="$PWD"' \
  atclone'PYENV_ROOT="$PWD" ./libexec/pyenv init - > zpyenv.zsh' \
  atpull"%atclone" src"zpyenv.zsh" nocompile'!' for \
    pyenv/pyenv
```

### `Bin-Gem-Node` profile

Provides the version manager via _shims_, i.e.: automatic forwarder scripts created under `$ZPFX/bin` (which is added to the `$PATH` by default by ZI). It needs the [bin-gem-node](https://github.com/z-shell/z-a-bin-gem-node) annex (it has the shim-creation feature).

The ZI command executed will be equivalent to:

```shell
zi as'null' lucid  atinit'export PYENV_ROOT="$PWD"' \
  atclone'PYENV_ROOT="$PWD" ./libexec/pyenv init - > zpyenv.zsh' \
  atpull"%atclone" src"zpyenv.zsh" nocompile'!' sbin"bin/pyenv" for \
    pyenv/pyenv
```

---

> This repository compatible with [ZI](https://github.com/z-shell/zi)

The [pyenv/pyenv](https://github.com/pyenv/pyenv) zsh package that uses the [zsh-string-lib](https://github.com/z-shell/zsh-string-lib) to automatically:

- get the plugin's Git repository OR release-package URL,
- get the list of the recommended ices for the plugin,
  - there can be multiple lists of ices,
  - the ice lists are stored in _profiles_; there's at least one profile, _default_,
  - the ices can be selectively overridden.
