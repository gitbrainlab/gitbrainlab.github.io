# Releases

`0.1.0-rc.1` is the initial experimental specification/reference-toolkit candidate. It does not authorize production bot adoption or establish a validated ontology implementation. Stable remains unset.

Resolve the current [discovery document](../.well-known/civicspec.json) for the pinned manifest URL and digest. Each manifest's `source_revision` selects the exact repository revision containing its components. Read [the publication protocol](../docs/publication.md) before consuming or publishing a release.

The manifest's component set excludes discovery and release manifests themselves. This avoids self-hash cycles and allows the mutable discovery pointer to advance independently. Old manifests and pinned source bytes remain inspectable.
