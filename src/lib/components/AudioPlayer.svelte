<script lang="ts">
	let {
		src,
		caption = '',
		allowDownload = false,
		allowRemotePlayback = false,
	}: {
		/** Path to audio source. */
		src: string;

		caption?: string;
		/** Autoplay the audio upon page load */

		allowDownload?: boolean;
		/** Allow casting via AirPlay and Miracast */
		allowRemotePlayback?: boolean;
	} = $props();

	let controlsList: string[] = [];
	if (!allowDownload) {
		controlsList.push('nodownload');
	}
	if (!allowRemotePlayback) {
		controlsList.push('noremoteplayback');
	}
</script>


<figure>
  <figcaption>{caption}</figcaption>
  <audio 
		controls
		controlslist="{controlsList.join(' ')}"
		preload="metadata"
		{src}
	></audio>

	{#if allowDownload}
  	<a href="{src}"> Download audio </a>
	{/if}
</figure>
