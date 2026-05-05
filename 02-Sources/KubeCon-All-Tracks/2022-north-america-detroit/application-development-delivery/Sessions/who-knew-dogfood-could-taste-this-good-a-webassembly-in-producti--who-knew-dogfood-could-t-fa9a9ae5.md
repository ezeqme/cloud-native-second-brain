---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Application + Development + Delivery"
themes: ["GitOps Delivery", "Runtime Containers"]
speakers: ["Taylor Thomas", "Brooks Townsend", "Cosmonic"]
sched_url: https://kccncna2022.sched.com/event/182Gl/who-knew-dogfood-could-taste-this-good-a-webassembly-in-production-story-taylor-thomas-brooks-townsend-cosmonic
youtube_search_url: https://www.youtube.com/results?search_query=Who+Knew+Dogfood+Could+Taste+This+Good%3F+A+WebAssembly+In+Production+Story+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Who Knew Dogfood Could Taste This Good? A WebAssembly In Production Story - Taylor Thomas & Brooks Townsend, Cosmonic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Application + Development + Delivery]]
- Temas: [[GitOps Delivery]], [[Runtime Containers]]
- País/cidade: United States / Detroit
- Speakers: Taylor Thomas, Brooks Townsend, Cosmonic
- Schedule: https://kccncna2022.sched.com/event/182Gl/who-knew-dogfood-could-taste-this-good-a-webassembly-in-production-story-taylor-thomas-brooks-townsend-cosmonic
- Busca YouTube: https://www.youtube.com/results?search_query=Who+Knew+Dogfood+Could+Taste+This+Good%3F+A+WebAssembly+In+Production+Story+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Who Knew Dogfood Could Taste This Good? A WebAssembly In Production Story.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Gl/who-knew-dogfood-could-taste-this-good-a-webassembly-in-production-story-taylor-thomas-brooks-townsend-cosmonic
- YouTube search: https://www.youtube.com/results?search_query=Who+Knew+Dogfood+Could+Taste+This+Good%3F+A+WebAssembly+In+Production+Story+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_OfS9zlblXc
- YouTube title: Who Knew Dogfood Could Taste This Good? A WebAssembly In Producti... Taylor Thomas & Brooks Townsend
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/who-knew-dogfood-could-taste-this-good-a-webassembly-in-production-sto/_OfS9zlblXc.txt
- Transcript chars: 39500
- Keywords: webassembly, platform, running, little, actually, wasm, everything, benefits, modules, security, sourcing, assembly, cosmonic, cosmotic, server, application, actual, reactive

### Resumo baseado na transcript

thank you everyone so uh this talk is titled who knew dog food could taste this good and then it is a web assembly and production story so let's go ahead and introduce ourselves real quick um I'll let Brooks introduce himself first yeah um Brooks Townsend lead software engineer at cosmonic and also I'm a maintainer of the cncf open source wasm Cloud which is the app runtime we'll talk a little bit about today I'm a part of this fun Venn diagram of people that knows Elixir or

### Excerpt da transcript

thank you everyone so uh this talk is titled who knew dog food could taste this good and then it is a web assembly and production story so let's go ahead and introduce ourselves real quick um I'll let Brooks introduce himself first yeah um Brooks Townsend lead software engineer at cosmonic and also I'm a maintainer of the cncf open source wasm Cloud which is the app runtime we'll talk a little bit about today I'm a part of this fun Venn diagram of people that knows Elixir or webassembly and rust that there's a very very small intersection in the middle there love doing demos and and yeah Taylor yeah so I am a director of engineering at cosmonic I am a restation do a lot of rust coding came from doing gopher stuff before and I am the co-creator of cresslet and bindle if you've been looking at anything in the web assembly space you've probably at least heard of creslit um that was something I was a maintainer of our creator of and then I'm also a general like serial open source maintainer I'm an Emeritus hell maintainer I was a core Helm maintainer for a long time so I wrote a good chunk of the helm 3 code when it first came out so you can either throw tomatoes at me later or Thank Me Later whichever one is your pick and so that's a little bit about us so what are we going to talk about today first off we're going to go over what webassembly is and just out of curiosity here how many people have heard of webassembly how many people have used it okay there we go that's what I thought so we're going to talk about it um a little bit in like what what web assembly is why it's important and then what is this whole Wasim cloud and cosmotic thingy this is setting kind of the the foundation for what we're going to show we did in production with all of this and then we'll go over the architecture of our our applications and how everything is working the Deep dive into individual things we thought would be most important to share the lessons on and then Lessons Learned From that and then after that we'll talk a little bit about what we're doing next so we have this saying if any of you have talked to us before you've probably heard us say this webassembly is neither web nor assembly which is kind of funny given its name um the big thing is that it's an open w3c standard and it first became popular for the web when it came out and because it's for it because it became popular in the web it has some things that the web desires and that's namely that it's safe and secure
