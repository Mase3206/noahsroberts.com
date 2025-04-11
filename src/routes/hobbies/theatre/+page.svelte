<script>
	import Show from "$lib/components/portfolio/Show.svelte";
	import DotSeparator from "$lib/components/DotSeparator.svelte";
</script>

<h1>Theatre.</h1>

<p>
	Here is a selection of the theatrical projects I am most proud of. My original samples use CC BY-SA-NC 4.0. Any other licenses for specific audio clips will be noted in the file name and in a license index file.
</p>

<h2>Related Updates</h2>

<p>(This feature has not been set up yet.)</p>
<!-- TODO: relevant updates -->

<DotSeparator />

<Show 
	title="The Adding Machine"
	author="Elmer Rice"
	details={[
		{
			name: "Genre",
			content: "Tragedy",
		},
		{
			name: "Performances",
			content: "April & May 2023",
		},
		{
			name: "Role",
			content: "Sound engineer, Sound designer, Assistant operator",
		},
		{
			name: "Timeline",
			content: "3 Months",
		},
	]}
>
	<p>
		Over the course of a few months, I worked closely with my director, <a href="https://shanebridgerlutz.wixsite.com/shanelutz">Bridger Lutz</a>, to create the acoustic aesthetic he envisioned. This included pulling sounds from royalty-free sound banks as well as making my own sounds if what we needed did not yet exist. With the help of QLab 5, I used over sixty unique sound files, including three homemade tracks, amounting to almost half a gigabyte of compressed and uncompressed audio to run the show.
	</p>
	<p>
		This was the first show where I was not afraid to shy away from my previous philosophy of simplicity a bit. I progressively added more and more elements to the show to push me out of my comfort zone and make it that much more impactful.
	</p>
	<p>
		I was training another student to take my place at the time, so I put him in charge of operating the sound during the show.
	</p>
	<p>
		Samples of this project are available upon request. Visit the <a href="/resume">Resume</a> page for my contact information.
	</p>
</Show>
