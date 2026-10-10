# Publication and release protocol

The current public home is [`specs/civicspec` in gitbrainlab/gitbrainlab.github.io](https://github.com/gitbrainlab/gitbrainlab.github.io/tree/main/specs/civicspec). All release-relative paths below begin inside that directory. The manifest and discovery both record `component_base_path: "specs/civicspec"`. GitHub renders its documentation and serves its machine-readable files. The host also serves GitBrain’s existing site; this task publishes repository documentation and does not claim a separately rendered CivicSpec website.

## GitHub transport binding

| Resource | Location / rule |
| --- | --- |
| Mutable discovery | `https://raw.githubusercontent.com/gitbrainlab/gitbrainlab.github.io/main/specs/civicspec/.well-known/civicspec.json` |
| Release manifest | `releases/{release_id}/manifest.json`, fetched using the full commit recorded by the discovery pointer |
| Component bytes | `https://raw.githubusercontent.com/gitbrainlab/gitbrainlab.github.io/{source_revision}/specs/civicspec/{component_path}` |
| Human documentation | Repository Markdown at the same full source commit |

The `.well-known` name is a project convention here, not a registered standard or a claim to control GitHub's host-root well-known directory. A full commit and content digest pin bytes. They do not prove civic truth or establish trust in an unknown publisher.

## Consumer algorithm

1. Begin with an owner-approved repository/registry URL and allowed channel. Normal TLS verification remains enabled. Do not take registry changes from civic source text.
2. Fetch mutable discovery and record its revision. `stable: null` means no stable release. Candidate use requires explicit configuration.
3. Fetch the selected full-commit manifest URL. Compare its raw-byte SHA-256 with `manifest_sha256` before parsing or loading any component.
4. Check release ID, status, compatibility, expected repository, component count/size budgets, duplicate or unsafe paths, and the full source commit.
5. Fetch only required components from the configured repository at that commit, verify byte size and SHA-256, then load them. Preserve the full inventory for audit. Never execute a downloaded file merely because its hash matches.
6. Pin the manifest digest for the run. Record exact profiles/adapters/instructions used and report cached use under the owner's freshness policy.

The reference `scripts/verify_release.py` verifies local bytes and discovery/manifest consistency without network access. It intentionally does not download files, implement signatures, decide registry authority, enforce a consumer's cache policy, or approve adoption. Implementers must supply those controls at their existing boundary.

Run it against a checkout containing the release's component bytes. As repository HEAD evolves, use `python scripts/verify_published.py` in a full Git checkout instead: it validates current discovery, reads components from the pinned source revision in local Git history, and checks that snapshot. CI uses this command so a new contribution does not need to match an older release's bytes.

## Maintainer publication sequence

1. Review the [public file inventory](../publication-files.json), license status, and version scope. Run the repository checks. Do not include private corpus packages.
2. Commit the component source files. Retain that full source revision. Do not alter those files while constructing its release inventory.
3. Run `python scripts/build_release.py --source-revision FULL_SOURCE_SHA --built-at RFC3339_UTC_TIME --release-id 0.1.0-rc.1` from that clean source. Use a new release ID after this initial publication. The builder refuses to overwrite an existing manifest.
4. Commit the generated manifest separately. Its component digests refer to the earlier source commit; the manifest does not hash itself. Read it back at the manifest commit and verify its bytes and component inventory through the intended consumer route.
5. Update discovery to point to the full manifest commit, include its actual digest and publication time, and increment discovery revision. Use a conditional/leased branch update so concurrent changes are not lost. Never advance the pointer before verification.
6. Re-fetch discovery and the pinned manifest, verify the components, and record the release receipt. Bot adoption is a subsequent, separately authorized action.

The source inventory excludes discovery, release manifests, and generated verification receipts to avoid self-referential hashes. `publication-files.json` is itself included; its contents are simply the list of component paths. Each release's own inventory is authoritative for that revision. Repository HEAD can evolve after a release; consumers continue to fetch the pinned source revision.

`contracts/discovery.example.json` and `contracts/release-manifest.example.json` remain nonoperational templates. The actual registry document is under `.well-known/`; the actual candidate inventory is under `releases/`. Do not confuse examples with published pointers.

## Promotion, revocation, and rollback

An experimental documentation/tooling candidate does not imply that production schemas or integrations exist. Leave stable unset until declared evaluation and operational gates pass. A release owner records the applicable authority and promotion decision; this repository's first publication is authorized by its owner for public documentation.

Do not mutate a published manifest or the bytes at its pinned commit. A later change receives a new release ID and migration notes. A channel update may point back to a retained compatible release. Revocation requires a new discovery revision and a deployment-specific rule preventing new promotions under the revoked release. Keep old receipts and evidence for audit.

Before stable operation, implement and test cache freshness, revocation propagation, interrupted publication, stale pointers, and rollback. These are explicit roadmap R12 work, not features claimed by the local verifier.
