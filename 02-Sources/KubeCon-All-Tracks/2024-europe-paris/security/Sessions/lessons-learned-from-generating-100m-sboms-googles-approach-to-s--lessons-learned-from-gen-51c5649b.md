---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security"]
speakers: ["Brandon Lum", "Isaac Hepworth", "Google"]
sched_url: https://kccnceu2024.sched.com/event/1YeQW/lessons-learned-from-generating-100m-sboms-googles-approach-to-sbom-compliance-brandon-lum-isaac-hepworth-google
youtube_search_url: https://www.youtube.com/results?search_query=Lessons+Learned+from+Generating+100M+SBOMs%3A+Google%E2%80%99s+Approach+to+SBOM+Compliance+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Lessons Learned from Generating 100M SBOMs: Google’s Approach to SBOM Compliance - Brandon Lum & Isaac Hepworth, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: Brandon Lum, Isaac Hepworth, Google
- Schedule: https://kccnceu2024.sched.com/event/1YeQW/lessons-learned-from-generating-100m-sboms-googles-approach-to-sbom-compliance-brandon-lum-isaac-hepworth-google
- Busca YouTube: https://www.youtube.com/results?search_query=Lessons+Learned+from+Generating+100M+SBOMs%3A+Google%E2%80%99s+Approach+to+SBOM+Compliance+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Lessons Learned from Generating 100M SBOMs: Google’s Approach to SBOM Compliance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQW/lessons-learned-from-generating-100m-sboms-googles-approach-to-sbom-compliance-brandon-lum-isaac-hepworth-google
- YouTube search: https://www.youtube.com/results?search_query=Lessons+Learned+from+Generating+100M+SBOMs%3A+Google%E2%80%99s+Approach+to+SBOM+Compliance+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZYsUbN6oT7Q
- YouTube title: Lessons Learned from Generating 100M SBOMs: Google’s Approach to SBOM Compliance
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/lessons-learned-from-generating-100m-sboms-googles-approach-to-sbom-co/ZYsUbN6oT7Q.txt
- Transcript chars: 38241
- Keywords: software, google, product, dependencies, supply, actually, executive, little, government, artifact, products, ingredients, requirements, dependency, builder, source, looking, document

### Resumo baseado na transcript

my name is Isaac heworth uh I'm a product manager at Google um I work a lot on supply chain stuff um I work on Google's own internal supply chain um I do a lot of work in open source as well um I chair the uh supply chain Integrity working group in op ssf um work closely with the the salsa team sigstore and and so on and I'm here with my colleague Brandon who'll introduce himself too I I'm Brandon um I'm a software engineer at Google I

### Excerpt da transcript

my name is Isaac heworth uh I'm a product manager at Google um I work a lot on supply chain stuff um I work on Google's own internal supply chain um I do a lot of work in open source as well um I chair the uh supply chain Integrity working group in op ssf um work closely with the the salsa team sigstore and and so on and I'm here with my colleague Brandon who'll introduce himself too I I'm Brandon um I'm a software engineer at Google I I work on software supply chain um as well as open source security um both concentrating on metadata what to do with it a lot of s bombs as we're going to talk a lot about today as Bon Vex um salsa and and all the Jazz um also involved with the cncf tax well awesome all right great well thanks for turning out to talk about es bombs quick show of hands before we get started who's heard of s bombs awesome okay who has heard of the US executive order um which specifies uh an esom requirement okay good showing all right this is good context let's begin um so we've got three things to talk about today we're going to talk generally about Google's Journey um through the sbom landscape over the last couple of years uh you know driven primarily in response to the executive order in the United States I'll talk a little bit about you know how we iteratively understood the assignment what are we supposed to be doing what does the executive order even say what does it mean how should we approach it uh brand is going to talk a little bit about you know our journey into the technical parts of es bom land the tooling and infrastructure we built you know how that played out the the types of properties we were looking for in es bombs how we guaranteed quality and so on um and then at the end brand and I are both going to share you know just a few of our hot takes uh some kind of you know insights or surprising things that we've learned on the journey uh and give you a sense of you know what's next uh so let's get started you know understanding the assignment um I I started uh you know I joined Google a few years ago and you know within a week or two of me joining Google um I received this email and the subject line is producing an s bomb for various ecosystems to meet the executive order uh and it had this ominous line at the bottom you know Isaac do you have bandwidth to drive this um and you know I was I was a couple of weeks in to to to Google and you know apart from like training and everything turns out I did have bandwidth to drive it u
