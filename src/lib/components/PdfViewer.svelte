<script>
	import Details from "./Details.svelte";

	let {
		file,
		altText,
		hiddenByDefault = true
	} = $props();
</script>

{#snippet viewer()}
<div>
	<object
		data="{file}"
		type="application/pdf"
		width="100%"
		height="600px"
		title="{altText}"
	></object>
	<a href="{file}">{altText}</a>
</div>
{/snippet}


{#if hiddenByDefault}
<Details summary="Preview file">
	{@render viewer()}
</Details>
{:else}
{@render viewer()}
{/if}