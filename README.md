# CER Feeds

Describes active Orcfax `currentExchangeRate` (CER) feeds for Orcfax publishing
and monitoring.

## Status

The document and repository are proposed standards for the Orcfax network for
the V1 rollout. We reserve the right to change the status and its content as our
network and client needs are better understood.

## Schema

<!-- markdownlint-disable -->

* **pair**: pair as described in-code, e.g. for the slug needed to trigger validation
* **label**: presentation label, e.g. for Orcfax explorer
* **interval**: heartbeat, integer, in seconds, e.g. `3600` == `3600 seconds == 1 hour`
* **deviation**: percentage deviation to monitor, integer, ex. `1` == `1%`
* **source**: ( `cex` | `dex` )
* **calculation**: ( `median` | `weighted mean` )
* **status**: (`paid` | `subsidized` | `showcase`)
* **type**: (`CER` ) `CER` == `currencyExchangeRate`

<!-- markdownlint-enable -->

Order of keys does not matter to JSON parsers, but it might provide important
visual cues to reviewers to maintain some consistency of ordering in this
document.

### Example

```json
        {
            "pair": "BASE-QUOTE",
            "label": "BASE-QUOTE",
            "interval": 3600,
            "deviation": 2,
            "source": "dex",
            "calculation": "weighted mean",
            "status": "showcase",
            "type": "CER"
        },
```

## Adding feeds

Try to add feeds in alphabetical order so they can be more easily audited then
once done, follow the versioning methodology set out below.

## Versioning

Calver is proposed. Changes should be made to the document locally. The metadata
should be updated with the anticipated calver number (`YYYY.MM.DD.NUMBER`) where
NUMBER represents the number of the release on a given day, e.g. if a feed is
updated twice in one day, the number  will be `0002`. A tag should be created
and pushed for the version as part of publishing.

### Tagging

Tagging should be connected to feed changes, and so might look as follows:

* `git tag -a 2024.08.06.0001 -m "price feeds: 2024.08.06.0001"`

### Accessing versions

The JSON can be accessed through different approaches. Some examples are shown
below for `2024.08.06.0001`. The tagged approach is preferred for precision.

Access examples:

* HEAD: `https://raw.githubusercontent.com/orcfax/cer-feeds/main/feeds/cer-feeds.json`
* Tagged: `https://raw.githubusercontent.com/orcfax/cer-feeds/2024.08.06.0001/feeds/cer-feeds.json`
* Commit: `https://raw.githubusercontent.com/orcfax/cer-feeds/73d567fe7cd7cc5993f01dc0acfa20e97f219a6e/feeds/cer-feeds.json`

#### Download

A tag can also be downloaded via the GitHub tag page, e.g. [2024.08.06.0001][#1]

[#1]: https://github.com/orcfax/cer-feeds/releases/tag/2024.08.06.0001
