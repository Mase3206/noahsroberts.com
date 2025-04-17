export function formatDate(
	/** UTC date string from YAML frontmatter */
	date: string,
	/** A string containing the BCP 47 language tag for the desired locale. Defaults to American English (en-US). */
	locale: string = "en-US"
) {
	let parsedDate = new Date(date)
	const options: Intl.DateTimeFormatOptions = {
		day: "numeric",
		month: "long",
		year: "numeric",
	}

	return new Intl.DateTimeFormat(locale, options).format(parsedDate)
}