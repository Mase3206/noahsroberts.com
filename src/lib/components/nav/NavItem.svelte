<script>
	let { children, href } = $props();
</script>

<li class="mb-2 md:ml-4 text-base">
	<a {href} class="no-underline hover:underline">
		{@render children()}
	</a>
</li>