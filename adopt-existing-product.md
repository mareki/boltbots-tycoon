# Adopt Agentic Harness 1.5.3 In An Existing Product

Copy the prompt below into a Codex task whose workspace is the existing Product repository.

```text
Stage Agentic Harness `1.5.3` from immutable tag
`20260930-1.5.3-remove-added-rules` in this existing Product repository.

1. Obtain `adopt-existing-product.sh` from that exact authenticated tag and run it with this
   repository root as `--target`. The command may create only `.agentic-harness/**`.
2. Do not overwrite or edit root instructions, routing, Product lifecycle, plans, code, or
   historical Contracts. If any Core collision, symlink, path escape, or source mismatch exists,
   stop without mutation.
3. Report the exact staged Harness identity and confirm activation is `inactive_staged`.
4. Inspect only the minimum existing root/routing/domain structure needed to propose a separate
   Product-owned integration and Context Coverage plan. Do not apply that plan without explicit
   Human approval.
5. Classify discovered Contexts only as `legacy_unmodeled`, `partially_modeled`, or
   `domain_model_effective`. Untouched legacy Contexts remain non-blocking; later work changing a
   Context needs an effective Foundation revision or an approved context-specific legacy exception.
6. Do not perform a big-bang domain rewrite or create ceremonial modules, ports, or adapters.
```

Fresh installation into an empty Product repository still uses `bootstrap.sh`. Replacing an
already installed Harness Core still uses the parameterless `upgrade-product.sh`.

Version `1.5.3` includes the protected Manifest → Operating Policy task-duty route. It becomes part
of Product task entry only through the separately authorized activation above; inactive staging
does not activate governance or grant permission to rewrite Product-owned entry files.
