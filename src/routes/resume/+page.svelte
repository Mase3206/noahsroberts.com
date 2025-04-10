<svelte:head>
	<title>Resume</title>
</svelte:head>

<script>
	import PdfViewer from '$lib/components/PdfViewer.svelte'
</script>

<h1>Resume.</h1>

<!-- TODO: Formatting -->
<p>
	Please don't hesitate to reach out with the contact information to the right. Samples of my projects are available upon request if public links are unavailable.
</p>

<p>
	noah@noahsroberts.com <br />
	Missoula, MT
</p>

<PdfViewer file="/assets/resume-apr-2024.pdf" altText="Resume (April 2024).pdf" />
