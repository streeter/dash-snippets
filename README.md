Dash Snippets
=============

Setup
-----

```sh
> git clone https://github.com/streeter/dash-snippets.git
> cd dash-snippets
> bundle install
> echo "DASH_SNIPPET_PATH=~/path/to/snippets.dash" > .env
> rake dash:dump
```

Make sure to setup the `DASH_SNIPPET_PATH` environment variable.

Installing Snippets
-------------------

Run the rake task to build all the snippets inside of the Dash database:

```sh
> rake dash:build
```

Emoji
-----

You can create and update the system-wide emoji snippets in Dash using the `update_emoji.py` script. This script reads the `.plist` file inside of [`Macmoji`](https://github.com/warpling/Macmoji) git submodule and then exports `.toml` files that the `rake dash:build` task reads. Update the submodule and then run `update_emoji.py` to populate the new emoji.

Credits
-------

Code adopted from [@tbpgr](https://github.com/tbpgr)'s [`dash_snippets_builder`](https://github.com/tbpgr/dash_snippets_builder) repository. The idea to search for it came from the [`Macmoji`](https://github.com/warpling/Macmoji) repo, which is a submodule, and where the emoji dictionary comes from.
