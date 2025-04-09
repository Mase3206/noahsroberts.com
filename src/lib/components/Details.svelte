<script lang="ts">
    import type { Snippet } from "svelte";

	let {
		summary,
		children,
	}: {
		summary: string;
		children: Snippet;
	} = $props();
</script>

<details>
	<summary>{summary}</summary>

	{@render children()}
</details>