---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Taylor Thomas", "Wasm WG Chair"]
sched_url: https://kccnceu2025.sched.com/event/1tcuY/project-lightning-talk-the-super-fast-tag-runtime-wasm-review-taylor-thomas-wasm-wg-chair
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+The+Super+Fast+TAG+Runtime+Wasm+Review+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: The Super Fast TAG Runtime Wasm Review - Taylor Thomas, Wasm WG Chair

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: United Kingdom / London
- Speakers: Taylor Thomas, Wasm WG Chair
- Schedule: https://kccnceu2025.sched.com/event/1tcuY/project-lightning-talk-the-super-fast-tag-runtime-wasm-review-taylor-thomas-wasm-wg-chair
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+The+Super+Fast+TAG+Runtime+Wasm+Review+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: The Super Fast TAG Runtime Wasm Review.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcuY/project-lightning-talk-the-super-fast-tag-runtime-wasm-review-taylor-thomas-wasm-wg-chair
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+The+Super+Fast+TAG+Runtime+Wasm+Review+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2fkWLe3OqQg
- YouTube title: Project Lightning Talk: The Super Fast TAG Runtime Wasm Review - Taylor Thomas, Wasm WG Chair
- Match score: 0.893
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-the-super-fast-tag-runtime-wasm-review/2fkWLe3OqQg.txt
- Transcript chars: 5778
- Keywords: wasm, runtime, projects, working, inside, everyone, involved, around, define, lightning, review, ecosystem, talking, questions, overview, essentially, binary, assembly

### Resumo baseado na transcript

So quick announcement um that uh they've kind of asked us to do as well for some of these things. If you are involved in the ecosystem and have been involved in the tags, there is a tag reboot coming.

### Excerpt da transcript

Thanks everyone. Welcome to uh this quick lightning talk. This is the super fast tag runtime review. I'm Taylor Thomas. I am a CNCF um WASM working group co uh co-chair. Um there's more about me too, but I'm not going to focus on that. We don't have enough time. So quick announcement um that uh they've kind of asked us to do as well for some of these things. If you are involved in the ecosystem and have been involved in the tags, there is a tag reboot coming. Um that is something that will affect the WASM stuff that I'm talking about in tag runtime. Um, so multiple TOC members and everyone's going to be around um in the halls and stuff if you have any questions. So with that, let's talk about WAM. The tag runtime group asked me to kind of give an overview of WAM and where it is. It's one of those emerging technologies out there. Most people have heard of. What's WAM? This is the super fast thing. You're going to get a quick fire hose of all of this. If you don't understand it all, come talk to me later. Um, WAM is essentially a very small VM.

You can consider it. Um, you can build it in any language. it it compiles down to a binary and then that binary is used inside of a WASM runtime or in browsers or whatever it might be and those those things all run on any of the supported architectures and and and oss that they can run on which is a lot. Why do we use web assembly? Well, it has a capability based security model which is just something that means you're explicitly granting it permissions to do every single thing that it can do. Um it's got essentially zero cold start time. It's very tiny. uh and I mean very tiny and it's also portable. So those are the big main benefits there. Now why do we use WOM in the cloud? Once again I said fire hose. Here's your fire hose. Uh there is a bunch of reasons why we use WASM in the cloud. If you look at why people first use it, which is why you've heard probably um about it is that it is very much a browser technology to start off, but it is not only for the browser. You we have open standards, sandboxed, small and fast, like all those kind of things we've talked about.

um like you you're not worrying about like all the image CVES because everything's sandboxed. You don't have a lot of dependencies contained in there. Um and so those are all things that we get from WASOM. Now what I really want to talk about because that's what everyone's here for is the project overview. This is not everything, but I wanted to call
