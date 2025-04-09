<script>
	let { file, altText } = $props();
</script>


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
