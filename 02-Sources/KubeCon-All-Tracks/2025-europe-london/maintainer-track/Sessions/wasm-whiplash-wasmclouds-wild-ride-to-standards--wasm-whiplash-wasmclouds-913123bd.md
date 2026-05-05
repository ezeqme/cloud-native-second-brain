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
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Brooks Townsend", "Cosmonic"]
sched_url: https://kccnceu2025.sched.com/event/1tcz9/wasm-whiplash-wasmclouds-wild-ride-to-standards-brooks-townsend-cosmonic
youtube_search_url: https://www.youtube.com/results?search_query=Wasm+Whiplash%3A+WasmCloud%27s+Wild+Ride+To+Standards+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Wasm Whiplash: WasmCloud's Wild Ride To Standards - Brooks Townsend, Cosmonic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Brooks Townsend, Cosmonic
- Schedule: https://kccnceu2025.sched.com/event/1tcz9/wasm-whiplash-wasmclouds-wild-ride-to-standards-brooks-townsend-cosmonic
- Busca YouTube: https://www.youtube.com/results?search_query=Wasm+Whiplash%3A+WasmCloud%27s+Wild+Ride+To+Standards+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Wasm Whiplash: WasmCloud's Wild Ride To Standards.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcz9/wasm-whiplash-wasmclouds-wild-ride-to-standards-brooks-townsend-cosmonic
- YouTube search: https://www.youtube.com/results?search_query=Wasm+Whiplash%3A+WasmCloud%27s+Wild+Ride+To+Standards+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lrA6gOpLWMw
- YouTube title: Wasm Whiplash: WasmCloud's Wild Ride To Standards - Brooks Townsend, Cosmonic
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/wasm-whiplash-wasmclouds-wild-ride-to-standards/lrA6gOpLWMw.txt
- Transcript chars: 27232
- Keywords: assembly, write, language, complex, protocol, application, standard, actually, working, binary, little, started, platform, writing, standards, developers, target, support

### Resumo baseado na transcript

Uh thank you so much for for coming to Wom Whiplash Womcloud's wild ride to standards. I hope that this is informative and inspiring for you as it is a therapy session for me to talk about our past mistakes and a wild ride over the last 5 years of working on WAMC cloud. It's implemented now on the server side things like that and then it works on any supported architecture. Now the problem is is we started writing a bunch of extensions you know things that you could do with web assembly like to make HTTP requests and we assumed that we would just like serialize the complex types to JSON so everybody can just And when you look at all of this and this is when we started looking at Wazi and we're like wow like that solves a lot of our problems. And this was the hardest lesson for us to learn at the time because we weren't very involved with Web Assembly standards.

### Excerpt da transcript

Hey everybody. Uh thank you so much for for coming to Wom Whiplash Womcloud's wild ride to standards. Uh this is actually my first talk in the maintainer track. So super excited to be here talking to other maintainers. I hope that this is informative and inspiring for you as it is a therapy session for me to talk about our past mistakes and a wild ride over the last 5 years of working on WAMC cloud. I'm a senior software engineer at Cosmonic. a CNCF was cloud maintainer which is now an incubating project. I've been with the project since its conception in 2019 coming out of Capital 1. Um a huge rust station uh and a big uh and very sad demo enthusiast because I actually have no demos for you today. It's my first time ever doing that. So I'm going to try to hold your attention and and hopefully this should be this should be fun. The last uh five years of working on this project. So for today going through the agenda I want to talk just a little bit about what WASM cloud is uh why it exists the origins the ideals why the project started in the first place what we built that differentiated us and what we built to even show up as a project in the space using a new technology of web assembly and talk about the standards that solved so many of our problems uh and just in general standards and why they matter now today was cloud is an incubating project in the CNCF F we're a WASM native application platform for deploying applications everywhere.

We use web assembly as the unit of compute rather than a container for an application. Uh which means that you can compile your code to this platform agnostic tiny binary to any cloud edge uh even even your own. Now just like containers need container native platforms to do their best work you know orchestration all of the things you see here at this conference uh web assembly needs the same thing. It needs wom native tools and that's what we've been providing uh for for quite a long time. But before we can think about where was cloud is now we need to take a little bit of a step back let's let's go all the way back to 2019 uh where we started and before was cloud was cloud it was actually called waxo suit a cloudnative execute uh exo suit for web assembly and I know what you're thinking that that is the coolest name and this is the coolest logo and that this talk is going to be all about the mistake of renaming to cloud unfortunately uh that is is not exactly where we're going to go, but you know, I I understand uh you
