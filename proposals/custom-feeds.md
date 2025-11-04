---
author: @waalge
status: draft
---

# Custom feeds :: Proposal

## Problem

1. People want to put their custom data on-chain
2. They want it reported via an oracle
3. Orcfax currently has no way to do this

We need a way that "customer" can get their data on-chain via Orcfax.
The solution needs to meet consumers' needs, and align with Orcfax's
belief in audit-ability.

## Solution

Custom, signed, data feeds.

Process:

1. Off-chain Registration:
   It is often not possible nor prudent to do all things on-chain.
   Consumer seeks Orcfax network approval and develop the data pipeline
   for the feed.
   In this step it is established: - The definition of the feed. - In particular, the data type that will appear in the fact statement body.
   This can treated simply as `Data` if desired. - It may also include additional verification checks. - In particular, signing. - The scheme of publication (see below). - An "owner" key is established. - All of this is published to a public repo.
   Probably orcfax github.
   It is also where it is made clear who is paying who for what.
2. On-chain Registration:
    - Registration inserts the feed into the register.
    - Consumer registers their feed with their "owner" key.
    - The register contains pointers to both the feed definition,
      the hot keys used for signing, and the data sources (ie servers/ endpoints)
3. Publishing Statements: - Data collectors will query the data sources.
   They will check signatures are valid with respect to the specified scheme and keys

- Collectors can then sign with data embedded as a bytestring (TBC) including the timestamp.

4. Update Registration:
    - Owner key can update some of the data fields.
      For example when the server updates.
    - There may be a lag time between an update,
      and Orcfax data collectors aligning with the new feed details.
      Customer is responsible for ensuring both feeds until data collectors have updated.
    - Customer may also seek to update offline registration.
      Customer is responsible to considering any impacts to downstream consumers.
5. Deregistration:
    - Owner can remove their registration.
      The feed will cease to be published.

### Off-chain Registration

The output of this stage is a "feed specification" document as part of the Orcfax Feed Register repo.

The feed specification includes:

- Feed definition
- Owner key

#### Feed definition

##### Source definition

The specific endpoints are to be found in the on-line registration.
The endpoints should be globally available, otherwise collection may fail.

Multiple endpoints are recommended.
Note that this is for redundancy: A collector will attempt to collect data from any of the endpoints, not all.
Each endpoint must provide the same or equivalent data.
Failure to do so may result in issues downstream.

Off-chain registration specifies the expected format of the response.
Orfax supports multiple permissible variations of serving data and signature:

- as a json with base64 or base16 encoded `{body: <body>, signature: <signature>}`
- as a json with signature in the header (base64 or base16)
- as above but in bytes

##### Collection definition

Data collectors request data from the data sources.

Data collectors do "Phase one" data validation.
Phase one validation may include:

- Signature : Key specified in the on-line registration
- Time bound: some kind of time check
- (TBC)

Orcfax can work with customers to tailor the needs of the definition.
Data collectors broadcast the results of their collection to validators.

Data collectors report the following errors:

- `Unreachable` - No server was reached.
- `ServerError` - No server responded a status code `200`.
  (Caveat: Redirects should be followed.)
- `Unparseable` - A server responded with `200`, but the data did not match the form the definition.
- `PhaseOneValidationFail` - Fails Phase One validation.

##### Validation & Aggregation definition

Validator definition parts:

1. Rerun phase one validation.
   Note that for time bounds this is relative to the collector's claimed time of collection.
   Any failure will result in collector not being part of the aggregation.
2. Phase two validation/ aggregation:
   This may involve logic applied to multiple collector results.

Phase two may fail in some cases if, say,
the divergence is too great, or there are too many reported errors,
or there is insufficient successful collector results.

The output is:

- the fact statement to be published on Cardano
- the "data trace" to be put on Arweave

##### Publish

A fact statement is of the form:

```ts
{
    id: X/<name>/<version>,
    created_at: Timestamp,
    body: Data,
}
```

This is the same as is currently in use.
Consumer data will be delivered inside `body`.

The feed id `version` is owner's key (raw bytes, **NOT** hex encoded).
It is up to the customer to communicate to downstream consumers
as to whether or not they ought to be verifying the full feed id (including version).

Orcfax must lay out some examples of feed definitions for customers to understand this stage.

### On-chain registration

The customer performs on-chain registration.
This is a transaction that creates an OrcfaxRegister token at the corresponding address
with an inline datum with the following data:

```ts
{
    owner: VerificationKey,
    info: {
        hot-key: VerificationKey (Scheme dependent),
        source: [<HTTP_ENDPOINT>],
        offline-registration-url: <URL>,
        repo-version: <GIT_HASH>,
    }
}
```

- A token is minted, with name equal to customers cold key
- Future (continuing) spends, (or end) must be singed by the owner key
- The hot key can be updated.
- Source info is probably : URL(s) and the expect request info (HTTP/JSON/BYTES).

The feed id will use the customer's cold key digest as the version.

- Other members of the validator network can independently verify the signatures
  and do not need to collect the data separately.

### Open questions

There are many open questions concerning how rigid or flexible this process ought to be.
Here are just some.

1. Data source schemes: do we support json and bytes

- Plutus data encoded.
- Data as bytestring

2. Phase one validation: do we support more than signatures.
   If so, we need to parse the bodies and extract, say, signatures.
   Which schemes and formats do we support?

3. What if there are multiple on-chain registrations of the same owner?

4. What precisely is the point of the on-chain registration?
