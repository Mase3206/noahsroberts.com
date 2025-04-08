<script>
	let { title, children } = $props();
</script>

<h1>{title}.</h1>

{@render children?.()}