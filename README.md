# ffc MkDocs Video

This plugin allows you to embed videos on the documentation pages using a simple Markdown syntax.

## Installation

Install the package with pip:

```bash
$ pip install ffc-mkdocs-video
```

Enable the plugin in the `mkdocs.yml` file:

```yaml
plugins:
    - ffc-mkdocs-video
```

> See how to use [MkDocs Plugins](https://www.mkdocs.org/dev-guide/plugins/#using-plugins)

## Usage

To add a video to the final documentation page, you need to use the Markdown syntax for images with a **specific name** *(hereinafter ***marker***)*.

> See how to use [Markdown syntax](https://guides.github.com/features/mastering-markdown/)

**Example:**

*content folder structure*

```
├── content
|   ├── ...
│   ├── video.md
│   └── videos
│       └── costa_rica.mp4
└── mkdocs.yml
```

*video.md*


## Configuration

### Marker

By default, the string `type:video` is used as a **marker** in the Markdown syntax.

You can change this value by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - ffc-mkdocs-video:
      mark: "custom-marker"
```

Now you can use this **marker** in the Markdown syntax:

```
![custom-marker](https://www.youtube.com/embed/LXb3EKWsInQ)
```

### Style

By default, the following CSS styles are used for the `<iframe>` tag that is inserted into the final page:

```css
position: relative;
width: 100%;
height: 22.172vw;
```

You can change the style by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - ffc-mkdocs-video:
      css_style:
        width: "100%"
        height: "22.172vw"
        ...
```

If embedded videos are too small on mobile browsers than adjust the height value to 100% to see if that resolves the problem.

### Autoplay

By default, the video autoplay is deactivated, you can enable the autoplay by adding the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - ffc-mkdocs-video:
      auto_play: "autoplay"
      ...
```

## Contributing

1.  Fork it.
2.  Create your feature branch:  `git checkout -b my-new-feature`
3.  Commit your changes:  `git commit -am 'Add some feature'`
4.  Push to the branch:  `git push origin my-new-feature`
5.  Submit a pull request

## License
The MIT License (MIT)

Copyright (c) 2021 Mikalai Lisitsa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
