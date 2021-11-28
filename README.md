<h3>

| **Package source:** |        Source Tarball        | Binary |        Git         | Node | Gem |
| :-----------------: | :--------------------------: | :----: | :----------------: | :--: | :-: |
|     **Status:**     | :heavy_check_mark: (default) |  :x:   | :heavy_check_mark: | :x:  | :x: |

</h3>

- [Introduction](#introduction)
- [Install](#install)
	- [Available `pack''` invocations](#available-pack-invocations)
	- [Default Profile](#default-profile)
	- [`Bin-Gem-Node` Profile](#bin-gem-node-profile)

# Introduction

> **[?]**
> This repository not compatible with previous versions (zplugin, zinit).
>
> Please upgrade to [ZI](https://github.com/z-shell-zi)

The [pyenv/pyenv](https://github.com/pyenv/pyenv) zsh package than can use the NPM package registry to automatically:

-   get the plugin's Git repository OR release-package URL,
-   get the list of the recommended ices for the plugin,
    -   there can be multiple lists of ices,
    -   the ice lists are stored in _profiles_; there's at least one profile, _default_,
    -   the ices can be selectively overridden.

# Install

## Available `pack''` invocations

```zsh
# Download the tarball with the default ice list
zi pack for pyenv

# Download the tarball with the bin-gem-node annex-utilizing ice list
zi pack"bgn" for pyenv

# Download with the bin-gem-node annex-utilizing ice list FROM GIT REPOSITORY
zi pack"bgn" git for pyenv
```

## Default Profile

Provides the `pyenv` version manager by extending `$PATH` to make it point into
the `bin` subdirectory of the plugin.

The ZI command executed will be equivalent to:

```zsh
zi lucid as'command' pick'bin/pyenv' atinit'export PYENV_ROOT="$PWD"' \
    atclone'PYENV_ROOT="$PWD" ./libexec/pyenv init - > zpyenv.zsh' \
    atpull"%atclone" src"zpyenv.zsh" nocompile'!' for \
        pyenv/pyenv
```

## `Bin-Gem-Node` Profile

Provides the version manager via _shims_, i.e.: automatic forwarder scripts created
under `$ZPFX/bin` (which is added to the `$PATH` by default by ZI). It needs the
[bin-gem-node](https://github.com/z-shell/z-a-bin-gem-node) annex (it has the
shim-creation feature).

The ZI command executed will be equivalent to:

```zsh
zi as'null' lucid  atinit'export PYENV_ROOT="$PWD"' \
    atclone'PYENV_ROOT="$PWD" ./libexec/pyenv init - > zpyenv.zsh' \
    atpull"%atclone" src"zpyenv.zsh" nocompile'!' sbin"bin/pyenv" for \
    pyenv/pyenv
```
