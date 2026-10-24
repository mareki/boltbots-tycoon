# Harness Release Manifest

> Artifact ID: `AH-RELEASE-1.5.3`  
> Artifact class: Generated view  
> Source owner/revision: `Master Harness Distribution / ca658bd2898570fea3f0dc20832dd7c70a339be8`  
> Generator/source: `AH-ASSEMBLER-001/0.2.0 / 0d1564a5bd5d1526e3afcadccf1a3952ac313de6535e947eabe653c57806184b`  

## Release Identity

Before task work, read `.agentic-harness/policies/operating-policy.md` and its task-wide
`.agentic-harness/core/work-management-and-execution.spec.md` §5.1 route. This protected bridge
also applies when an older Product-owned root entry file names only this Manifest. Ordinary Human
wording suffices; entry and Preflight are not exempt. Verify the external trust anchor/inventory
before relying on the payload. This route grants no initialization, mutation or Brownfield activation.

- Harness version: `1.5.3`
- Release channel: `stable`
- Master repository: `https://github.com/langvis/agentic_harness.git`
- Release tag: `20260930-1.5.3-remove-added-rules`
- Source commit: `ca658bd2898570fea3f0dc20832dd7c70a339be8`
- Protected-payload tree SHA-256: `a9a1e42c5aa369d9d7f866544c62a9c0a1623ad7a8291b3daf8152a847443be8`
- Overlay schema: `1`
- Supported starting versions/schemas: `[{"kind":"fresh_install"},{"version":"1.0.0","overlay_schema":"1"},{"version":"1.0.1","overlay_schema":"1"},{"version":"1.0.2","overlay_schema":"1"},{"version":"1.0.3","overlay_schema":"1"},{"version":"1.0.4","overlay_schema":"1"},{"version":"1.0.5","overlay_schema":"1"},{"version":"1.0.6","overlay_schema":"1"},{"version":"1.0.7","overlay_schema":"1"},{"version":"1.0.8","overlay_schema":"1"},{"version":"1.0.9","overlay_schema":"1"},{"version":"1.0.10","overlay_schema":"1"},{"version":"1.0.11","overlay_schema":"1"},{"version":"1.0.12","overlay_schema":"1"},{"version":"1.0.13","overlay_schema":"1"},{"version":"1.1.0","overlay_schema":"1"},{"version":"1.1.1","overlay_schema":"1"},{"version":"1.2.0","overlay_schema":"1"},{"version":"1.2.1","overlay_schema":"1"},{"version":"1.2.2","overlay_schema":"1"},{"version":"1.2.3","overlay_schema":"1"},{"version":"1.2.4","overlay_schema":"1"},{"version":"1.2.5","overlay_schema":"1"},{"version":"1.2.6","overlay_schema":"1"},{"version":"1.2.7","overlay_schema":"1"},{"version":"1.3.0","overlay_schema":"1"},{"version":"1.3.1","overlay_schema":"1"},{"version":"1.3.2","overlay_schema":"1"},{"version":"1.4.0","overlay_schema":"1"},{"version":"1.4.1","overlay_schema":"1"},{"version":"1.5.0","overlay_schema":"1"},{"version":"1.5.1","overlay_schema":"1"},{"version":"1.5.2","overlay_schema":"1"}]`
- Required adjacent history: `["AH-HISTORY-1-0-0-TO-1-0-1","AH-HISTORY-1-0-1-TO-1-0-2","AH-HISTORY-1-0-2-TO-1-0-3","AH-HISTORY-1-0-3-TO-1-0-4","AH-HISTORY-1-0-4-TO-1-0-5","AH-HISTORY-1-0-5-TO-1-0-6","AH-HISTORY-1-0-6-TO-1-0-7","AH-HISTORY-1-0-7-TO-1-0-8","AH-HISTORY-1-0-8-TO-1-0-9","AH-HISTORY-1-0-9-TO-1-0-10","AH-HISTORY-1-0-10-TO-1-0-11","AH-HISTORY-1-0-11-TO-1-0-12","AH-HISTORY-1-0-12-TO-1-0-13","AH-HISTORY-1-0-13-TO-1-1-0","AH-HISTORY-1-1-0-TO-1-1-1","AH-HISTORY-1-1-1-TO-1-2-0","AH-HISTORY-1-2-0-TO-1-2-1","AH-HISTORY-1-2-1-TO-1-2-2","AH-HISTORY-1-2-2-TO-1-2-3","AH-HISTORY-1-2-3-TO-1-2-4","AH-HISTORY-1-2-4-TO-1-2-5","AH-HISTORY-1-2-5-TO-1-2-6","AH-HISTORY-1-2-6-TO-1-2-7","AH-HISTORY-1-2-7-TO-1-3-0","AH-HISTORY-1-3-0-TO-1-3-1","AH-HISTORY-1-3-1-TO-1-3-2","AH-HISTORY-1-3-2-TO-1-4-0","AH-HISTORY-1-4-0-TO-1-4-1","AH-HISTORY-1-4-1-TO-1-5-0","AH-HISTORY-1-5-0-TO-1-5-1","AH-HISTORY-1-5-1-TO-1-5-2","AH-HISTORY-1-5-2-TO-1-5-3"]`
- Release notes reference: `docs/releases/1.5.3.md`
- Manifest trust anchor: signed release attestation or expected manifest SHA-256 supplied outside this installed boundary
- Protected Release Metadata: `.agentic-harness/release-metadata.json`
- Release Evidence Policy SHA-256: `49875b3cd9ed511b05e955762c53f15e1396519c0293139b73b89fc16d7dbf25`
- External Release Attestation SHA-256: `95617eae933a4f1c69dfd2eae2999c40f0fe39e51684d290a196190252bd811b`

## Available Bundled Profiles

| Profile ID | Version | SHA-256 | Installed path |
|---|---|---|---|
| `AH-PROFILE-AWS-SERVERLESS-MVP-001` | `0.2.1` | `72fd666556791156b5711b12f8a8ae3dfb381370c43c78ef94573028905a9288` | `.agentic-harness/core/aws-serverless-mvp-profile.spec.md` |

Product selection is recorded in the human-approved Product Technical Delta, not in this immutable release manifest.

## Protected File Inventory

The release assembler inventories every regular file under `.agentic-harness/**` except this manifest. Symlinks are forbidden. Root and Product files are outside the compatible-upgrade ownership boundary. This manifest does not hash itself; its own digest is authenticated by the external trust anchor.

| Installed path | Payload class | Source artifact ID/version | SHA-256 |
|---|---|---|---|
| `.agentic-harness/core/agent-collaboration-and-approval.spec.md` | `Harness specification` | `AH-SPEC-COLLABORATION-001/2.0.2` | `d19d971906e9b649622eb9bbe68907abd08bb8cccc4575516c12c590f778fa2c` |
| `.agentic-harness/core/artifact-and-source-of-truth.spec.md` | `Harness specification` | `AH-SPEC-ARTIFACTS-001/1.0.2` | `2946973a269d8effa337bce26c0ba8ac36e3923ceba2014eda024ebc88a40147` |
| `.agentic-harness/core/aws-serverless-mvp-profile.spec.md` | `Profile` | `AH-PROFILE-AWS-SERVERLESS-MVP-001/0.2.1` | `72fd666556791156b5711b12f8a8ae3dfb381370c43c78ef94573028905a9288` |
| `.agentic-harness/core/delivery-staging-and-recovery.spec.md` | `Harness specification` | `AH-SPEC-DELIVERY-001/1.0.4` | `a9b2cfe0d8015a7f4096cce47d1543f45e3e2d6d1de3195a37f2de164ae5ac3c` |
| `.agentic-harness/core/design-system-and-visual-review.spec.md` | `Harness specification` | `AH-SPEC-DESIGN-001/0.6.0` | `09baee3eb8af323c9ed9a10960e8ae35e62ba3aa9a103010d4f5c650d900c17c` |
| `.agentic-harness/core/domain-modeling-and-bounded-context-architecture.spec.md` | `Harness specification` | `AH-SPEC-DOMAIN-001/1.1.1` | `ff5e48ff016cf116edc3069e9430eb395ef6e3fa7eb92ea71f4a3bb2ae21b36e` |
| `.agentic-harness/core/evaluation-and-enforcement.spec.md` | `Harness specification` | `AH-SPEC-EVALUATION-001/0.19.3` | `863d237bb96ff6b1c3d95d6a6e0a1f355ff0117032dba4cba759f0dd248c9726` |
| `.agentic-harness/core/harness-constitution.spec.md` | `Constitutional` | `AH-CONSTITUTION-001/0.5.0` | `c50c34baa97524e64440ef467b1a0f9744ed10dcbc20a7cbffef402c58f8b2d8` |
| `.agentic-harness/core/harness-distribution-and-bootstrap.spec.md` | `Harness specification` | `AH-SPEC-DISTRIBUTION-001/1.0.3` | `78cc9a66194062243884baedd0351960af2dcbd54b7226eb1bc0d23df7b90dec` |
| `.agentic-harness/core/harness-evolution-and-versioning.spec.md` | `Harness specification` | `AH-SPEC-EVOLUTION-001/1.0.2` | `c46b6f1a6b3cb05d2559fbac5adc0ae9f30b29c75888a671388553cc4b818f90` |
| `.agentic-harness/core/near-zero-idle-cost-architecture.spec.md` | `Harness specification` | `AH-SPEC-COST-001/0.1.0` | `b7a97538d7a2e822fa97a30a8a522eaf6713fcebcb1bf08adaf91ba439b5d216` |
| `.agentic-harness/core/ordinary-correction-and-amendment-authority.spec.md` | `Harness specification` | `AH-SPEC-CORRECTION-AUTHORITY-001/3.0.1` | `3d5896d4000e8eaf4b2698700294792701b8cdb4663909b7d065444fda472c86` |
| `.agentic-harness/core/ordinary-run-admission-and-transition-integrity.spec.md` | `Harness specification` | `AH-SPEC-ORDINARY-ADMISSION-001/3.0.4` | `dd9795f382fc2e2421c65834292c984a5ad1abb22e5f2f9e9d3289e013e5fcc9` |
| `.agentic-harness/core/product-agnostic-engineering-baseline.spec.md` | `Harness specification` | `AH-SPEC-ENGINEERING-001/0.4.1` | `666203ce4755efe8787dd91edc2be03285c9635f046029ff63441ae62b939460` |
| `.agentic-harness/core/product-initialization-and-planning.spec.md` | `Harness specification` | `AH-SPEC-INITIALIZATION-001/0.6.2` | `d805f653b425c64e6bbfcf67bf0e5befbd0015d783b067cddcc3fbe968df9071` |
| `.agentic-harness/core/product-release-versioning.spec.md` | `Harness specification` | `AH-SPEC-PRODUCT-RELEASE-001/0.2.2` | `ae0b30bf6bb799a1ab3e790d8c7494bda2ad025181befc2b7e544b972431f504` |
| `.agentic-harness/core/routing.md` | `Navigation` | `AH-OVERLAY:.agentic-harness/core/routing.md@1.5.3` | `9f2bfab4f8a3ea67b6fa1a1b1f0a2771fe58ef3b98224d8091ade843a39dc43a` |
| `.agentic-harness/core/work-management-and-execution.spec.md` | `Harness specification` | `AH-SPEC-WORK-001/2.0.4` | `ab9451652eb1c5b0319e4ae0124a91345eea153763e0b2d6c63e3ea150239e32` |
| `.agentic-harness/history/1.0.0--1.0.1.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.0--1.0.1.md@1.5.3` | `398da1a15b7f0fa047e9d38427c6596b8f27631143f121e69d8a1ba02481c9c9` |
| `.agentic-harness/history/1.0.1--1.0.2.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.1--1.0.2.md@1.5.3` | `3429d1b1923084294932fc0c35033a11fd143bd6df4867e6e8d6c8b96806fc35` |
| `.agentic-harness/history/1.0.10--1.0.11.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.10--1.0.11.md@1.5.3` | `21b16bac19df162988ea48d0981366ea711f43a1c1d832642dc5826122050b17` |
| `.agentic-harness/history/1.0.11--1.0.12.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.11--1.0.12.md@1.5.3` | `6d9520e1442f36c4c0886d80ee426bcc38125c469482f3c4960c651a77fb50ea` |
| `.agentic-harness/history/1.0.12--1.0.13.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.12--1.0.13.md@1.5.3` | `7a7d1fba61c7df4d19d268db9b52264cffcb6ac8db7164539e9b23b8b49d6aa9` |
| `.agentic-harness/history/1.0.13--1.1.0.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.13--1.1.0.md@1.5.3` | `429f9932cee9b835a4fd81c707f511eb1da1ad2ef95770849980577de42a3d31` |
| `.agentic-harness/history/1.0.2--1.0.3.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.2--1.0.3.md@1.5.3` | `2cd78e41c817bad7cdd8bc0f6d6437196970db8dbad553c8698f7f8c12486ac3` |
| `.agentic-harness/history/1.0.3--1.0.4.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.3--1.0.4.md@1.5.3` | `13bdc9755734d24469f9c67a88d4f8f6498f5ae433792a88aec2a5e45176be0c` |
| `.agentic-harness/history/1.0.4--1.0.5.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.4--1.0.5.md@1.5.3` | `85168124623faad5eb4a633ecb96b265c5cbd3cbaa0162f9de1760baae6526a6` |
| `.agentic-harness/history/1.0.5--1.0.6.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.5--1.0.6.md@1.5.3` | `ed2184b1cab471c0788e2620d798f2af8207cc019d1db81a073ecdc7d3062388` |
| `.agentic-harness/history/1.0.6--1.0.7.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.6--1.0.7.md@1.5.3` | `41eb713c4c71fb01c7f1c3452c4b07199dfb630e3206dae890f0c7d0bfd111df` |
| `.agentic-harness/history/1.0.7--1.0.8.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.7--1.0.8.md@1.5.3` | `15307a05adee4988d66b4610cfcffd0d2d83054519036427e1218696c377ea3c` |
| `.agentic-harness/history/1.0.8--1.0.9.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.8--1.0.9.md@1.5.3` | `4f784c4fdbbafacb8e2fa1ad7983d5fc52a136a81697402d799f0261d07e7661` |
| `.agentic-harness/history/1.0.9--1.0.10.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.0.9--1.0.10.md@1.5.3` | `8950c164d0a7395286bdf0401db423884d038ff72f7f0bba04d12a58ddd86bc6` |
| `.agentic-harness/history/1.1.0--1.1.1.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.1.0--1.1.1.md@1.5.3` | `e737b2105bedfdfc54c232712efde64e734482826d1e0ac72104f824e416fed7` |
| `.agentic-harness/history/1.1.1--1.2.0.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.1.1--1.2.0.md@1.5.3` | `b1d48d37af5a84e3b2a73614e1ec3f3220ac18e957a37718a6b64d74f593e899` |
| `.agentic-harness/history/1.2.0--1.2.1.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.2.0--1.2.1.md@1.5.3` | `dfd9bdf5b982fb512b0110e1df442d84387dd2cc13d4ede6741dfb43ef4e7375` |
| `.agentic-harness/history/1.2.1--1.2.2.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.2.1--1.2.2.md@1.5.3` | `a9dd7dccd664239a40c3fe0a44ef783f3624dd8cf372491ad903ec233eeec693` |
| `.agentic-harness/history/1.2.2--1.2.3.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.2.2--1.2.3.md@1.5.3` | `13eae23b3f6b467b3cb987a5dfa787a82230a2c2b4d75bf24b24d79e8e207e15` |
| `.agentic-harness/history/1.2.3--1.2.4.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.2.3--1.2.4.md@1.5.3` | `f57c5062c51e720031c18e41f001baee3e15fc86b9c3dfd314a10c5b32af27cd` |
| `.agentic-harness/history/1.2.4--1.2.5.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.2.4--1.2.5.md@1.5.3` | `98de8e89e3e2a41f317da6863e2178e1496392b1fc5e79a6b367177fbd8d01cc` |
| `.agentic-harness/history/1.2.5--1.2.6.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.2.5--1.2.6.md@1.5.3` | `f26ebf922b155e0c785738c38d6139540fec01cd1eb0e6dcf04c07b4e4fe7a34` |
| `.agentic-harness/history/1.2.6--1.2.7.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.2.6--1.2.7.md@1.5.3` | `f2e2225125a126960d15d093e9f8d49f8125525a1f3a355bdb36c9918ba27092` |
| `.agentic-harness/history/1.2.7--1.3.0.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.2.7--1.3.0.md@1.5.3` | `372a959e925745e5fb32f26bdf56463afe85d3b70dab24ff52206f2ac5cbce30` |
| `.agentic-harness/history/1.3.0--1.3.1.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.3.0--1.3.1.md@1.5.3` | `e6dc22a0bdd40f553d9504cb6b0c03cff25a835657fb0107ebe1e8b8b31baacf` |
| `.agentic-harness/history/1.3.1--1.3.2.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.3.1--1.3.2.md@1.5.3` | `355b47244d7acd4d10bfc0dea471db9e6e42268abfe3b31aba17a1d787fa4a41` |
| `.agentic-harness/history/1.3.2--1.4.0.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.3.2--1.4.0.md@1.5.3` | `e9818e9bb84a39550211baa2ba402ba6eec282f3c1883c37131a5c09daf414b5` |
| `.agentic-harness/history/1.4.0--1.4.1.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.4.0--1.4.1.md@1.5.3` | `b8313318340269ee134af79370accab891a53e4a8d083d92d1043e63a1537ea3` |
| `.agentic-harness/history/1.4.1--1.5.0.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.4.1--1.5.0.md@1.5.3` | `c96061e8d281ede10588763c9e9e481916b5d7f26e49acf9738fd0d46dac5ca1` |
| `.agentic-harness/history/1.5.0--1.5.1.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.5.0--1.5.1.md@1.5.3` | `b9e9149da5dd0888c4b7b63c427553df50dcd334c02674925b551f51c4b040c2` |
| `.agentic-harness/history/1.5.1--1.5.2.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.5.1--1.5.2.md@1.5.3` | `a08390cf5446ff42b394509444233eb29427129337262b2ff3046c4e786a515f` |
| `.agentic-harness/history/1.5.2--1.5.3.md` | `Reference` | `AH-OVERLAY:.agentic-harness/history/1.5.2--1.5.3.md@1.5.3` | `7cb0c85db4e2e00ee5fe1ed0f0cd91807c4efb6a28cc0bee505d3f9789ccb274` |
| `.agentic-harness/policies/operating-policy.md` | `Navigation` | `AH-OVERLAY:.agentic-harness/policies/operating-policy.md@1.5.3` | `88a3af3fdbbfe660e33c56aa24d40842afe22f47bb4905ac473168377f4ad5e1` |
| `.agentic-harness/release-metadata.json` | `Reference` | `AH-OVERLAY:.agentic-harness/release-metadata.json@1.5.3` | `ebddb7e44410e130bea7eae56e1efbf7f88f093bb87811d1b5ec7bcf45a6532c` |
| `.agentic-harness/roles/spawn-reviewer.md` | `Generated view` | `AH-OVERLAY:.agentic-harness/roles/spawn-reviewer.md@1.5.3` | `bb86db33efe7807f0e078c04cc0bf8828886f59027f05cc032746aa372e59659` |
| `.agentic-harness/roles/team.md` | `Navigation` | `AH-OVERLAY:.agentic-harness/roles/team.md@1.5.3` | `40856689bbaf9680aae2afc8447d2cd7ec1f69649b60eb9b10fd625ce3ed8872` |
| `.agentic-harness/templates/README.md` | `Navigation` | `AH-OVERLAY:.agentic-harness/templates/README.md@1.5.3` | `597bf93344064657d252b43c3ea9427678c09d0f44c0c6ba337ea27b0db0c0ed` |
| `.agentic-harness/templates/architecture-proposal.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/architecture-proposal.template.md@1.5.3` | `f8082ef959bf317d2afb7f7c5612eadf2d0c20cf62639224853ada7fae0f2dba` |
| `.agentic-harness/templates/bootstrap-and-installation-state.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/bootstrap-and-installation-state.template.md@1.5.3` | `b6d7c7ccfd9fc1ee8a1f8ba1c301cecba07484e51e8d10d45b656f9569177bc7` |
| `.agentic-harness/templates/brownfield-adoption-state.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/brownfield-adoption-state.template.md@1.5.3` | `0ff33929c58b8c7a60394e1e89c7d4abdcf5da52126dc3164b05d9d9a2bd1870` |
| `.agentic-harness/templates/checkpoint-and-evidence.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/checkpoint-and-evidence.template.md@1.5.3` | `af4fa758952ec59802cd54421d45842f840e307bc77b8168cd40b8bc8ee151ba` |
| `.agentic-harness/templates/contract-spec.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/contract-spec.template.md@1.5.3` | `472b60a7bc7155a02696378887f90a12cccc83f1508406bbedeae4f3c0e65ed6` |
| `.agentic-harness/templates/decision-record.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/decision-record.template.md@1.5.3` | `7ab56d6f065ac0b83f79188b83de02b52fad5957bf4c55628cd3dfb85e1fd953` |
| `.agentic-harness/templates/delivery-slice.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/delivery-slice.template.md@1.5.3` | `ff4b39e56fb373073b5de4a0f544fd2fe8229044ddaeb591017e1f1ee9ea71f6` |
| `.agentic-harness/templates/design-system-and-flow.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/design-system-and-flow.template.md@1.5.3` | `77f7ac63593d607e78e066efe035c62c67018bbadf759009bc7ec6094b4e835c` |
| `.agentic-harness/templates/domain-foundation-review-pack.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/domain-foundation-review-pack.template.md@1.5.3` | `0974f342ca26ff8dda30c1c3387231bc2f790e3fa4638f222ec69c6b612b7cb5` |
| `.agentic-harness/templates/domain-foundation.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/domain-foundation.template.md@1.5.3` | `2b8b4bacf759a9f1f82713bf3a1b10f9ec30ca81dbe40352295815ffb89fd561` |
| `.agentic-harness/templates/domain-spec.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/domain-spec.template.md@1.5.3` | `6af7b71f069891125281b8aa5e696db81b1dfbb90224e6e9d1462d9e71c78b9a` |
| `.agentic-harness/templates/eval-case.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/eval-case.template.md@1.5.3` | `c75826964d45a81705c781efa084bd0e1c68bf9ffa653d613dacac30097f4812` |
| `.agentic-harness/templates/execution-run.template.md` | `Work contract` | `AH-OVERLAY:.agentic-harness/templates/execution-run.template.md@1.5.3` | `f573da743fc2dcf3b667c82061ec2eb1572b8ad97d322c79440c172daf49d1f7` |
| `.agentic-harness/templates/harness-improvement-proposal.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/harness-improvement-proposal.template.md@1.5.3` | `f6a5e4bd6f58c73a2feae376da7816579210768975f3d50f43df72bb874b6785` |
| `.agentic-harness/templates/harness-log.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/harness-log.template.md@1.5.3` | `07f5de49028c42970249098a5a35740cfac2883bd1b045da56e24d14f0432800` |
| `.agentic-harness/templates/initialization-review-pack.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/initialization-review-pack.template.md@1.5.3` | `40b53772447e2212e32f30e0d939384382b4240a4bb366bfcff15cf07e321956` |
| `.agentic-harness/templates/milestone-and-six-week-plan.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/milestone-and-six-week-plan.template.md@1.5.3` | `4ae36ba702791ce8d1f97f9743e999c11e398e249fd55d69873b97346447b8f3` |
| `.agentic-harness/templates/module-entry-map.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/module-entry-map.template.md@1.5.3` | `9066bc5e854ccaa45356b6ebfe873df4a8841592466ffdd3b4c464b0721b5bbd` |
| `.agentic-harness/templates/orchestration-spec.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/orchestration-spec.template.md@1.5.3` | `f530bf92b0719f28ca229044e77624668cba5105c5e6ff7c3b8c19bcf4ba4e64` |
| `.agentic-harness/templates/product-delivery-rc-manifest.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/product-delivery-rc-manifest.template.md@1.5.3` | `f0030c4244dd70e4637a54ea0c515323dfe5cdc5c53d04faee27502e208e9cae` |
| `.agentic-harness/templates/product-harness-upgrade.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/product-harness-upgrade.template.md@1.5.3` | `13ae10987eac7bb222f6fcf9faed1873249669552ee662b2ac180765d4094c9b` |
| `.agentic-harness/templates/product-release-identity-event.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/product-release-identity-event.template.md@1.5.3` | `b42398bd22eb3c735d354b59c71e69aaf131e67dfaab029617508e3cc57b27d5` |
| `.agentic-harness/templates/product-release-policy.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/product-release-policy.template.md@1.5.3` | `24082028d7dd7e52af4d86c8b6b034c5df51b490e1e29302c87d730d5e6e78a0` |
| `.agentic-harness/templates/product-release-record.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/product-release-record.template.md@1.5.3` | `bf1cb1c3ca043b5aebe38bc06e15be314cf9b78cae204b316694f3460d7c3627` |
| `.agentic-harness/templates/product-technical-delta.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/product-technical-delta.template.md@1.5.3` | `159ff77f1fb1a33f1bbb978988cd96c0333c5000cfa380fd84e8f04c3f299356` |
| `.agentic-harness/templates/product-vision-brief.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/product-vision-brief.template.md@1.5.3` | `82dded6b9792d458c304d85aa50da960be848a63bf1f12a887ecc044d7bf4451` |
| `.agentic-harness/templates/requirement-and-use-case-register.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/requirement-and-use-case-register.template.md@1.5.3` | `8817ec9ed709b9c3b5fb487688f408d4494185a76e528281ea21ff7cd2c17d65` |
| `.agentic-harness/templates/review-record.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/review-record.template.md@1.5.3` | `ea8f52d99cd2e7e1ab898611057ce3c5c54e0fae927dafa7ea72da3df930fbea` |
| `.agentic-harness/templates/technical-risk-experiment.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/technical-risk-experiment.template.md@1.5.3` | `a6572e47447e8dddafb4e0051fdd402370bc07eeeaed8fe67db63311131d1f98` |
| `.agentic-harness/templates/work-package.template.md` | `Reference` | `AH-OVERLAY:.agentic-harness/templates/work-package.template.md@1.5.3` | `2c7b4f2ca98faeeb48846994853099954ea2f2dce73bf533995a7f401df9425f` |
| `.agentic-harness/validators/README.md` | `Navigation` | `AH-OVERLAY:.agentic-harness/validators/README.md@1.5.3` | `86c8df7812f2414687f180508a7fd48232ccb5c8a9e959c342d139fe128f7221` |
| `.agentic-harness/validators/validate_harness.py` | `Reference` | `AH-OVERLAY:.agentic-harness/validators/validate_harness.py@1.5.3` | `ea77a06c9a43f9449f714c1c6c5a528bf6dd149e4a5e5d1f21ddace7271250e5` |
| `.agentic-harness/workflows/adopt-existing-product.md` | `Generated view` | `AH-OVERLAY:.agentic-harness/workflows/adopt-existing-product.md@1.5.3` | `780624f2bd4e3cb2e05849fb3cf0a393a54d0db48234f97c8d46cbfc1836d99d` |
| `.agentic-harness/workflows/execute-work.md` | `Generated view` | `AH-OVERLAY:.agentic-harness/workflows/execute-work.md@1.5.3` | `01488ca33875e8593e6386d7505705375b050560cc7937fd0a6844f18b41e533` |
| `.agentic-harness/workflows/harness-logging.md` | `Generated view` | `AH-OVERLAY:.agentic-harness/workflows/harness-logging.md@1.5.3` | `6f9230b48560d5787d7f348c0b3ea0e88dd84ce4d478953a4fce71028cbf4f8d` |
| `.agentic-harness/workflows/initialize-product.md` | `Generated view` | `AH-OVERLAY:.agentic-harness/workflows/initialize-product.md@1.5.3` | `e46c42297ad543aca8c37db76a6ed0fe8138999b45c3c2eccd2f8bdb3a2f65b1` |
| `.agentic-harness/workflows/promote-production.md` | `Generated view` | `AH-OVERLAY:.agentic-harness/workflows/promote-production.md@1.5.3` | `3be97648d10669f6244a67d3783b7c7224dc39fc62ebd32ea66193a60d2e8b4e` |
| `.agentic-harness/workflows/propose-harness-improvement.md` | `Generated view` | `AH-OVERLAY:.agentic-harness/workflows/propose-harness-improvement.md@1.5.3` | `c9e3828d7a2db92e44e4eba54e684e43a04d9a6fde7b776030ef62bf1348887f` |
| `.agentic-harness/workflows/resume-work.md` | `Generated view` | `AH-OVERLAY:.agentic-harness/workflows/resume-work.md@1.5.3` | `b93ee95852828dccbe8d6f307a7d9ba723ae44fcf5d304af97a25010f8ecaa7c` |
| `.agentic-harness/workflows/upgrade-harness.md` | `Generated view` | `AH-OVERLAY:.agentic-harness/workflows/upgrade-harness.md@1.5.3` | `c2c6ad53c40bfa80129fa7d0398b886d41bc7afc6ce8d536158de958e951039d` |

## Boundaries

- Protected and replaceable by compatible upgrade: `.agentic-harness/**`
- Seeded during bootstrap, then Product-owned: root `AGENTS.md`, `README.md`, `docs/**`, and other paths outside `.agentic-harness/**`
- Human-owned, Agent-read-only input: `product-input/**`
- Product-owned: `docs/**`, application/domain/orchestration/platform/package/test code, provider configuration allowed by active specs
- Harness learning proposals: `docs/harness-proposals/**`

New installations receive root `AGENTS.md` only as a stable entry router; current release-specific policy remains inside `.agentic-harness/**`. A legacy Product may retain an older root upgrade gate. That higher entry instruction is not silently superseded: the explicit Human upgrade prompt must override it for the exact compatible Core replacement. No Product-owned file is changed.

## Verification

Run `python3 .agentic-harness/validators/validate_harness.py --root . --mode product --expected-manifest-sha256 <external-sha256>` with the externally trusted expected manifest digest. The
read-only verifier hashes the raw Manifest and protected inventory/tree using
`AH-SPEC-DISTRIBUTION-001`. Product-owned checks use the responsible Git inventory, not an
unrestricted filesystem scan; root `AGENTS.md` is Product-owned and additional Agent-instruction
files are forbidden. The installer/workflow retains verification evidence only in its authorized
state boundary; the verifier never repairs Core or changes Product files. Any unresolved release/
install token, trust-anchor or inventory mismatch, unauthorized instruction file or unsupported
schema blocks Product mutation. Template markers under `.agentic-harness/templates/**` remain inputs.
