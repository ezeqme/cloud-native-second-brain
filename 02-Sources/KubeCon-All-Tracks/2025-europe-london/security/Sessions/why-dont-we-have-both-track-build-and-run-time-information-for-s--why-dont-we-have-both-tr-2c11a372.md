---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["Security"]
speakers: ["Jeff Mendoza", "Kusari", "Ben Hirschberg", "ARMO"]
sched_url: https://kccnceu2025.sched.com/event/1tx7x/why-dont-we-have-both-track-build-and-run-time-information-for-security-with-kubescape-and-guac-jeff-mendoza-kusari-ben-hirschberg-armo
youtube_search_url: https://www.youtube.com/results?search_query=Why+Don%E2%80%99t+We+Have+Both%3F+Track+Build-+and+Run-time+Information+for+Security+With+Kubescape+and+GUAC+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Why Don’t We Have Both? Track Build- and Run-time Information for Security With Kubescape and GUAC - Jeff Mendoza, Kusari & Ben Hirschberg, ARMO

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United Kingdom / London
- Speakers: Jeff Mendoza, Kusari, Ben Hirschberg, ARMO
- Schedule: https://kccnceu2025.sched.com/event/1tx7x/why-dont-we-have-both-track-build-and-run-time-information-for-security-with-kubescape-and-guac-jeff-mendoza-kusari-ben-hirschberg-armo
- Busca YouTube: https://www.youtube.com/results?search_query=Why+Don%E2%80%99t+We+Have+Both%3F+Track+Build-+and+Run-time+Information+for+Security+With+Kubescape+and+GUAC+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Why Don’t We Have Both? Track Build- and Run-time Information for Security With Kubescape and GUAC.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7x/why-dont-we-have-both-track-build-and-run-time-information-for-security-with-kubescape-and-guac-jeff-mendoza-kusari-ben-hirschberg-armo
- YouTube search: https://www.youtube.com/results?search_query=Why+Don%E2%80%99t+We+Have+Both%3F+Track+Build-+and+Run-time+Information+for+Security+With+Kubescape+and+GUAC+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=x5qguW0SF_I
- YouTube title: Why Don’t We Have Both? Track Build- and Run-time Information for S... Jeff Mendoza & Ben Hirschberg
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/why-dont-we-have-both-track-build-and-run-time-information-for-securit/x5qguW0SF_I.txt
- Transcript chars: 24411
- Keywords: sbombs, packages, runtime, software, filtered, server, vulnerabilities, security, little, running, collector, ebpf, source, container, vulnerability, cubecape, actually, around

### Resumo baseado na transcript

And and we're here today to talk about um both build time, runtime, sbomb, supply chain information in your clusters um using both Kubcape and Guac. Um I'm a software engineer at Kusari which is a software supply chain uh security startup and I'm a maintainer of Guac which is an open SSF project uh licensed Apache 2.0. Um so Cubescape uh started u like four years ago the project um it used to be uh it started as uh CLI for scanning Kubernetes and uh live API and YAML files uh for misconfigurations from a security perspective. uh it originally it was really built upon um uh open policy agent and implemented a lot of lot of uh uh controls security controls frameworks and so on and the project really fastly evolved into a full-fledged Kubernetes security platform. So both you can cube cubecape has a version of as a that can be installed as an operator in your kubernetes cluster and it covers uh quite a lot of things that you would need u from a security perspective when managing a cluster and kubernetes doesn't give you that out of the box uh you know we started by from configuration scanning uh we have a vulnerability scanner which is going to be I think the focal point of the discussion today.

### Excerpt da transcript

Hello everyone. Thanks for being here today. Uh my name is Jeff Mendoza. Hey everyone, I'm Ben. I good to have everyone here today. Yeah. And and we're here today to talk about um both build time, runtime, sbomb, supply chain information in your clusters um using both Kubcape and Guac. Uh okay, a little background about myself. Um I'm a software engineer at Kusari which is a software supply chain uh security startup and I'm a maintainer of Guac which is an open SSF project uh licensed Apache 2.0. Um so I'm also involved in a couple other open SSF projects and also the clearly defined project. So I said before as I said before I'm Ben uh maintainer one of the maintainers of uh Cubscape which is a we'll talk a little bit later about that uh but it's a Kubernetes security uh platform uh and the CNCF incubating project um and I'm coming mostly from software engineering and the security product side of the industry uh just a brief overview of the the talk we're going to talk a little bit about the two projects and then um some exciting new features that have just launched and a demo.

All right, so I'm gonna um bring you all up to speed on GUK. Uh GUAK stands for it's a backronym. You know, we like avocados and and guacamole, but it stands for graph for understanding artifact uh now I I forgot what the C was composition. Um, so what it is is a system that you you bring up and it's uh at the core of it is a GraphQL API. Um, but it it pulls in all kinds of supply chain data um from all kinds of sources or types of documents. Primarily software bill of materials sbomb, but also um salsa addestations, scorecard scores, uh vex documents, things like that. and it brings it all into a a system that you're able to use uh those GraphQL queries to drive insights about your entire supply chain. So if an SBOM just contains um the the contents of a single piece of software, you get all of those into one big graph and you start seeing the interconnection between all of your software. Um the way you typically use it is at least up until now is you would have like a step in your build that would generate an sbomb and then um ingest or upload that sbomb into the guac system that you're running.

Um to dive a little bit more into um the different components that make up Guac, uh what you see here in green is the core core project of Guac. um the the database and assembler is uh what runs the API. Um but there's a a lot of other pieces that sit around it. So for example, the inge
