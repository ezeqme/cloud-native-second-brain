---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Shivay Lamba", "Meilisearch", "Kevin Hoffman", "Cosmonic"]
sched_url: https://kccncna2023.sched.com/event/1RQZf/bringing-cloud-native-wasm-to-the-mainstream-with-wasm-working-group-shivay-lamba-meilisearch-kevin-hoffman-cosmonic
youtube_search_url: https://www.youtube.com/results?search_query=Bringing+Cloud+Native+WASM+to+the+mainstream+with+WASM+Working+Group+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Bringing Cloud Native WASM to the mainstream with WASM Working Group - Shivay Lamba, Meilisearch & Kevin Hoffman, Cosmonic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Shivay Lamba, Meilisearch, Kevin Hoffman, Cosmonic
- Schedule: https://kccncna2023.sched.com/event/1RQZf/bringing-cloud-native-wasm-to-the-mainstream-with-wasm-working-group-shivay-lamba-meilisearch-kevin-hoffman-cosmonic
- Busca YouTube: https://www.youtube.com/results?search_query=Bringing+Cloud+Native+WASM+to+the+mainstream+with+WASM+Working+Group+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Bringing Cloud Native WASM to the mainstream with WASM Working Group.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1RQZf/bringing-cloud-native-wasm-to-the-mainstream-with-wasm-working-group-shivay-lamba-meilisearch-kevin-hoffman-cosmonic
- YouTube search: https://www.youtube.com/results?search_query=Bringing+Cloud+Native+WASM+to+the+mainstream+with+WASM+Working+Group+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=b1675UWMLas
- YouTube title: Bringing Cloud Native WASM to the mainstream with WASM Working Group - Shivay Lamba & Kevin Hoffman
- Match score: 0.914
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/bringing-cloud-native-wasm-to-the-mainstream-with-wasm-working-group/b1675UWMLas.txt
- Transcript chars: 31148
- Keywords: assembly, course, working, module, actually, runtime, native, modules, workloads, projects, landscape, access, wasm, basically, running, ecosystem, interested, machine

### Resumo baseado na transcript

so welcome everyone I know we are kind of at towards the end of cucon so I hope everyone had a great cubec con uh super excited to be presenting at my first ever like in-person cubec con outside of the collocated event so uh super excited for that and super also excited to introduce the webm working group to the masses um for today's talk so if all of you are interested in learning more about web assembly or are working in a cloud native uh startup or in

### Excerpt da transcript

so welcome everyone I know we are kind of at towards the end of cucon so I hope everyone had a great cubec con uh super excited to be presenting at my first ever like in-person cubec con outside of the collocated event so uh super excited for that and super also excited to introduce the webm working group to the masses um for today's talk so if all of you are interested in learning more about web assembly or are working in a cloud native uh startup or in a project and are looking at ways in which you could in like you know introduce web assembly uh or just curious about webassembly in general uh this talk will be cated for all of you and will be helpful and hopefully by the end uh you'll be motivated enough to join the working group and like just help you know increase the adoption of web assembly so I'm Shai I'm a developer relations in at M search and with me we have Kevin who is a director of engineering at s India over to you sure all right so let's it's uh last day of cubec con 2:00 in the afternoon everybody's in a food coma so uh who wants to see some really cool demos yeah we have none of those so uh the agenda here basically what I want to do is cover what web assembly is why we should care about it um what it has to do with the cloud and then we'll get into the cncf uh web assembly working group and you know some of the things that we'd like you to do to help out and contribute so actually before I get into there did did anybody attend the collocated web assembly event earlier this week okay uh who here has deployed web assembly somewhere not on a browser okay well you don't count all right so uh not too many so web assembly is a stack-based virtual machine it is designed to be portable secure small and fast and uh coincidentally those are pretty much the main criteria we have for deploying uh applications in the cloud so when we say portable that means that web assembly is CPU and Os agnostic it can't access the operating system the kernel file system I'll explain the little red asterisk there later um you can interpret the web assembly code or you can uh jit compile it into native code it all depends on your needs uh web assembly modules are not supposed to be used as uh shared libraries they're not a replacement for dlls Orso files and uh at least for when you're building on Rust there are two different uh Target types one for regular web assembly and one for wzy and I'll get into what wazzy is in a minute so uh as far as security as I said th
