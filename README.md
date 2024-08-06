# Price Feeds

Describes active Orcfax feeds for Orcfax publishing and monitoring.

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
* **status**: (`sponsored` | `subsidized` | `showcase`)
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

Access via:

* HEAD: `https://raw.githubusercontent.com/orcfax/price-feeds/main/feeds/price-feeds.json`
* Tagged: `https://raw.githubusercontent.com/orcfax/price-feeds/2024.08.06.0001/feeds/price-feeds.json`
* Commit: `https://raw.githubusercontent.com/orcfax/price-feeds/97940c30407da79a6389386b1e7ad9500e06cf50/feeds/price-feeds.json`
