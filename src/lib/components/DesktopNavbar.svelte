<!-- Header.svelte -->
<style lang="scss">
	a {
		text-decoration: none;
		&:hover {
			text-decoration: underline;
		}
	}
	header {
		margin-left: 2em;
		margin-right: 2em;
		padding: 0em;
	}
	#siteTitle {
		font-size: 20px;
	}
	#items {
		* {
			font-size: 15px;
		}
	}
</style>

<header>
	<a href="/" id="siteTitle">Noah S. Roberts</a>

	<nav id="items">
		<ul>
			<!-- <li>
				<a href="/blog">Blog</a>
			</li>
			<li>
				<a href="/about">About</a>
			</li> -->
			<li>
				<a href="/resume">Resume</a>
			</li>
		</ul>
	</nav>
</header>