---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Matei David", "Buoyant"]
sched_url: https://kccnceu2024.sched.com/event/1YeOR/kubernetes-controllers-in-rust-fast-safe-sane-matei-david-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Controllers+in+Rust%3A+Fast%2C+Safe%2C+Sane+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Controllers in Rust: Fast, Safe, Sane - Matei David, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Matei David, Buoyant
- Schedule: https://kccnceu2024.sched.com/event/1YeOR/kubernetes-controllers-in-rust-fast-safe-sane-matei-david-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Controllers+in+Rust%3A+Fast%2C+Safe%2C+Sane+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Controllers in Rust: Fast, Safe, Sane.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOR/kubernetes-controllers-in-rust-fast-safe-sane-matei-david-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Controllers+in+Rust%3A+Fast%2C+Safe%2C+Sane+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rXS-3hFYVjc
- YouTube title: Kubernetes Controllers in Rust: Fast, Safe, Sane - Matei David, Buoyant
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-controllers-in-rust-fast-safe-sane/rXS-3hFYVjc.txt
- Transcript chars: 34302
- Keywords: controller, actually, controllers, basically, server, client, resource, resources, create, runtime, function, everything, application, little, cubert, probably, library, wanted

### Resumo baseado na transcript

um my name is mate I am a Linker maintainer I work for a company called buyant uh where I'm a software engineer you can reach out to me on social media um I'm on Twitter probably should have changed the logo uh you can find me on GitHub and a couple of slack channels um so yeah welcome to another talk on why you should rewrite your software and rust um the hype train is very very real and it's not stopping it's gone strong um and I've got

### Excerpt da transcript

um my name is mate I am a Linker maintainer I work for a company called buyant uh where I'm a software engineer you can reach out to me on social media um I'm on Twitter probably should have changed the logo uh you can find me on GitHub and a couple of slack channels um so yeah welcome to another talk on why you should rewrite your software and rust um the hype train is very very real and it's not stopping it's gone strong um and I've got a lot of things that I actually want to cover in this session so you know kind of a housekeeping thing who here has written a controller before doesn't matter what language it was in all right all right that helps me out uh what about rust any experience with rust all right and service meshes okay well that makes my job much much easier um so we have a couple of rations in a room uh but I still need to go through the slide you know like why rust um uh you know kind of the the topic of the stock one because it's fast right you can do your own memory allocations that's very important when you're working with software where latency is important where it's important that you manage data in a very uh efficient way um and rust lets you do that in a very nice way it has a very nice uh concurrent API you can do concurrency with a bunch of tools that were written uh with performance in mind uh back pressure is applied in a nice and elegant way and overall it's just a a very nice language to work with if you want to get stuff done fast but more so than that it's safe um right like uh you you don't basically have the same issues that you have with a with a language like C++ because the compiler really helps you out you have a bunch of invariants that it basically upholds to ensure that your code is safe uh whether that's in concurrent execution environments uh or whether that's in a single threed application you know that all holds you have ownership semantics uh you have marker Tri to ensure that uh you don't share data across threads when it's not meant to be shared uh and that makes the language really really safe to program in even if you don't have experience with managing your own memory and last but not least it's sane all right so you might have noticed this is exactly the the title of my talk but it's saying because the compiler really helps you out if you have to work with rust and you have an issue where your code doesn't compile uh the compiler is going to give you some very helpful output that's going to help you resolv
