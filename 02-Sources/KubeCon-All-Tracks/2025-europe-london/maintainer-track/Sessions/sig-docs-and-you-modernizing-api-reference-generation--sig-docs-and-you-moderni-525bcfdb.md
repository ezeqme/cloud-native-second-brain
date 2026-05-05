---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Kat Cosgrove", "Xander Grzywinski", "Independent"]
sched_url: https://kccnceu2025.sched.com/event/1td0V/sig-docs-and-you-modernizing-api-reference-generation-kat-cosgrove-xander-grzywinski-independent
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Docs+and+You%3A+Modernizing+API+Reference+Generation+CNCF+KubeCon+2025
slides: []
status: parsed
---

# SIG Docs and You: Modernizing API Reference Generation - Kat Cosgrove & Xander Grzywinski, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Kat Cosgrove, Xander Grzywinski, Independent
- Schedule: https://kccnceu2025.sched.com/event/1td0V/sig-docs-and-you-modernizing-api-reference-generation-kat-cosgrove-xander-grzywinski-independent
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Docs+and+You%3A+Modernizing+API+Reference+Generation+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre SIG Docs and You: Modernizing API Reference Generation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td0V/sig-docs-and-you-modernizing-api-reference-generation-kat-cosgrove-xander-grzywinski-independent
- YouTube search: https://www.youtube.com/results?search_query=SIG+Docs+and+You%3A+Modernizing+API+Reference+Generation+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RdT6P5x_fDM
- YouTube title: SIG Docs and You: Modernizing API Reference Generation - Kat Cosgrove & Xander Grzywinski
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sig-docs-and-you-modernizing-api-reference-generation/RdT6P5x_fDM.txt
- Transcript chars: 7972
- Keywords: reference, process, actually, pretty, release, contributors, generation, single, xander, documentation, website, expected, generated, entirely, existing, modernizing, maintainer, currently

### Resumo baseado na transcript

We were betting on how many people would come to this talk because nobody comes to maintainer track talks. Um, and Xander bet uh less than seven and we have unfortunately beat that number. And then we have to set some confusing build variables that will repeatedly be a problem for you while you're trying to do this entire process. Um, and you know, this is something that we would love to get some contributors jumping in to maybe start thinking about the design for this and what it could look like. Um but you know the Kubernetes API is it's it's open API spec so there is tooling out there for this um so if anyone is familiar with the open API ecosystem um ideally when we move forward with a rewrite we'd be able to

### Excerpt da transcript

We were betting on how many people would come to this talk because nobody comes to maintainer track talks. Um, and Xander bet uh less than seven and we have unfortunately beat that number. Thank you. Thank you. Uh, welcome to SIG Docs and you modernizing API reference generation. My name is Cat Cosgrove and I work for Wayland Utani. Uh, I am Xander Jerbinsky and I currently work for Shinra. Oh, I guess I should mention that we're both uh SIG docs technical leads, which is obviously why we're giving a talk on the maintainer track. But uh we're going to talk about the process for generating the API reference docs for Kubernetes and cube control. Um first I'm going to describe the current process. Note that everything I'm going to go through here is something that has to be done twice. once for Kubernetes and once for cube control which is lovely and not at all inconvenient. So uh the first thing we have to do is create a local workspace and set our go paths and then get a local clone of several repositories.

Um this starts out pretty pretty easy, pretty straightforward. This is all documentation from the uh Kubernetes website. You also need the K website repo and the KK repo which you have to rename for some reason that remains a mystery to me because I did not build this tool. And then we have to set some confusing build variables that will repeatedly be a problem for you while you're trying to do this entire process. Um, it's it's worth noting that this tool is actually uh a bash script that calls a Python script that calls several Go scripts, which is normal and sensible way to uh build software. This has to be done for every single release twice. So, we need a versioned directory and we've got to fetch the open API spec. This is also pretty easy at this point. Things are going well. Um, you're not going to run into any problems just yet. All of this is going to go smoothly and but it it will go off the rails pretty rapidly. This is where things start to go off the rails. Um, I am not quite sure why this tends to fail so hard.

Um, but it does every single time. Um, all we're doing is making the copy API and generating those two files. But this is usually going to barf. Um, this is this is straightforward. We're just modifying some markdown. Um, but this does have to be done for every single release. It is manual. It is annoying. It is consistent across releases. You always have to do this. So, it does seem like uh a thing we could automate or a thing th
