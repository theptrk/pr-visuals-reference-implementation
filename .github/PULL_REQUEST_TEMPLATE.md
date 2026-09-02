## Visual index

<!--
This template follows docs/pr-visual-review-style-guide.md.
Keep the sections that apply; delete the ones that do not.
Sections appear only when the PR touches what they describe.
-->

### 📊 Schema changes

<!--
Table rows use the action vocabulary and color semantics:
🟢 + create/add · 🟠 ~ rename · 🔵 % alter · 🔴 − drop
Never omit a change from the diff — omission is only an explicit count.
-->

| Change | Table | Column | Type |
|---|---|---|---|
| 🟢 `+ CREATE TABLE` | | | |

<details>
<summary>Raw changes</summary>

```diff
+ CREATE TABLE ...
```

</details>

### 🧭 Schema diff diagram

<!--
Commit the Graphviz ERD under docs/assets/ and reference it here.
Include the dot source in a <details> block so reviewers can regenerate it.
-->

![](docs/assets/schema.svg)

### 🎬 Affected flows

<!--
Mermaid sequenceDiagram for touched flows. GitHub renders it natively.
-->

```mermaid
sequenceDiagram
```

### Vocabulary

Colors and verbs per the pinned
[schema action vocabulary](docs/pr-visual-review-style-guide.md#2-action-vocabulary).
