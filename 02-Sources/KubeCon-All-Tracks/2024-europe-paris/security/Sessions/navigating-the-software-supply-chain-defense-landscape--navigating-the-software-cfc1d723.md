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
themes: ["AI ML", "Security"]
speakers: ["Marina Moore", "Aditya Sirish A Yelgundhalli", "New York University"]
sched_url: https://kccnceu2024.sched.com/event/1YeO3/navigating-the-software-supply-chain-defense-landscape-marina-moore-aditya-sirish-a-yelgundhalli-new-york-university
youtube_search_url: https://www.youtube.com/results?search_query=Navigating+the+Software+Supply+Chain+Defense+Landscape+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Navigating the Software Supply Chain Defense Landscape - Marina Moore & Aditya Sirish A Yelgundhalli, New York University

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: France / Paris
- Speakers: Marina Moore, Aditya Sirish A Yelgundhalli, New York University
- Schedule: https://kccnceu2024.sched.com/event/1YeO3/navigating-the-software-supply-chain-defense-landscape-marina-moore-aditya-sirish-a-yelgundhalli-new-york-university
- Busca YouTube: https://www.youtube.com/results?search_query=Navigating+the+Software+Supply+Chain+Defense+Landscape+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Navigating the Software Supply Chain Defense Landscape.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeO3/navigating-the-software-supply-chain-defense-landscape-marina-moore-aditya-sirish-a-yelgundhalli-new-york-university
- YouTube search: https://www.youtube.com/results?search_query=Navigating+the+Software+Supply+Chain+Defense+Landscape+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NzIHD4vPKVc
- YouTube title: Navigating the Software Supply Chain Defense Landscape - Marina Moore & Aditya Sirish A Yelgundhalli
- Match score: 0.8
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/navigating-the-software-supply-chain-defense-landscape/NzIHD4vPKVc.txt
- Transcript chars: 22820
- Keywords: supply, software, security, actually, source, requirements, projects, mapping, effort, attestations, together, question, process, number, securing, practices, probably, problems

### Resumo baseado na transcript

hopefully you're all here for our talk about navigating the software supply chain defense landscape um thank you all for coming um and we'll just get into it first of all a little bit about us um I'm Marina Moore I'm a PhD candidate at NYU as well as a maintainer of a number of open source security projects including tough in Toto and upan and I'm also a co-chair of tag security um hi and I'm AIA I'm also a PhD candidate at NYU I do a bunch of

### Excerpt da transcript

hopefully you're all here for our talk about navigating the software supply chain defense landscape um thank you all for coming um and we'll just get into it first of all a little bit about us um I'm Marina Moore I'm a PhD candidate at NYU as well as a maintainer of a number of open source security projects including tough in Toto and upan and I'm also a co-chair of tag security um hi and I'm AIA I'm also a PhD candidate at NYU I do a bunch of open source and software supply chain security uh uh I'm one of the maintainers of intoto and a few other things like the parts of intoto specification I'm the maintainer of giu over at the op ssf sandbox and I've contributed to a bunch of cncf and other open ssf efforts as well so given that you're all in the room uh you probably really care about your software supply chain and actually securing it and I'm guessing a part of that reason is because of the massive increase in software supply chain attacks we've seen in the last few years uh with like a ridiculous number of like high-profile numbers uh incidents as well um and the other reason why you probably care about it is uh all of those attacks has led to the form creation of new regulations in the United States in the EU that require you to uh care about securing your software supply chain as well so and and you you know uh as as someone who's sort of new to the space you're obviously going to be like okay where do I start how do I you know start securing my software supply chain do I create this thing called an esom or software build of materials that I keep hearing about and and does my esom you know solve all my problems and should I be signing my sbom or my software releases and who should sign it and who actually verifies these signatures if we actually sign it all of these questions that just keep coming up and at the end of it you're like is there like a to that I can just deploy and it does all of these things for me all of my software supply chain security problems are solved and let me just look this up and see what shows up and then you suddenly hit with a ridiculous number of tools again that that all have the software supply chain uh keyword somewhere in there because they're all just solving different like you know parts of it and this can also be really overwhelming right and again these are all just like uh most of these are just like uh open source tools and uh projects a couple of them are Maybe uh platforms but none of them really are like com
