---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Abu Kashem", "Red Hat Inc.", "Stefan Schimanski", "Upbound"]
sched_url: https://kccnceu2025.sched.com/event/1tx89/the-life-or-death-of-a-kubernetes-api-request-2025-edition-abu-kashem-red-hat-inc-stefan-schimanski-upbound
youtube_search_url: https://www.youtube.com/results?search_query=The+Life+%28or+Death%29+of+a+Kubernetes+API+Request%2C+2025+Edition+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Life (or Death) of a Kubernetes API Request, 2025 Edition - Abu Kashem, Red Hat Inc. & Stefan Schimanski, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Abu Kashem, Red Hat Inc., Stefan Schimanski, Upbound
- Schedule: https://kccnceu2025.sched.com/event/1tx89/the-life-or-death-of-a-kubernetes-api-request-2025-edition-abu-kashem-red-hat-inc-stefan-schimanski-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=The+Life+%28or+Death%29+of+a+Kubernetes+API+Request%2C+2025+Edition+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Life (or Death) of a Kubernetes API Request, 2025 Edition.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx89/the-life-or-death-of-a-kubernetes-api-request-2025-edition-abu-kashem-red-hat-inc-stefan-schimanski-upbound
- YouTube search: https://www.youtube.com/results?search_query=The+Life+%28or+Death%29+of+a+Kubernetes+API+Request%2C+2025+Edition+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Hc0jj-654lA
- YouTube title: The Life (or Death) of a Kubernetes API Request, 2025 Edition - Abu Kashem & Stefan Schimanski
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-life-or-death-of-a-kubernetes-api-request-2025-edition/Hc0jj-654lA.txt
- Transcript chars: 27672
- Keywords: request, server, handler, basically, object, timeout, happens, response, context, create, version, internal, routine, client, deadline, requests, resource, seconds

### Resumo baseado na transcript

I'm Stefan Shimanssky working on API server since ages 10 years or something. Um have touched a lot of the things we will show here and I have with me Abu I'm a software engineer at Red Hat and a similar history about API servers. This is jobs lowerase plural and this one is an uppercase word singular and this is already not trivial in Kubernetes um how this mapping actually happens and of course um when the request is done it's a post request to a URL and there's a uh returned and this means success so a batch is created but everything in between we want to talk through now so um this mapping um you will have heard about kinds and resources in kubernetes And um the kind is the one in The API server serves discovery and QC cuttle will query that which um returns all resources with the kinds served under the resources and lots of other meta information and in kubernetus we call that a rest mapping. So we basically pinpoint the exact location where the panic was where where the panic originated from and then it logs the u error and the stack trace and then it also panics here and this is by design so that it can let the HTTP server decide what to do with the panic.

### Excerpt da transcript

Welcome to our talk uh about life or death. I think we have to go away from the speakers. Uh life or death of a Kubernetes request, API request. I'm Stefan Shimanssky working on API server since ages 10 years or something. Um have touched a lot of the things we will show here and I have with me Abu I'm a software engineer at Red Hat and a similar history about API servers. So um what we want to do today we want to talk about API requests obviously but imagine you're sitting in this interview right you want to apply for a job or you're applying and there's this interviewer next to you and a very um common question is um and you will maybe experience something in a similar context API server is of course a topic but um you get asked so you do that right you you type qle create minus v9 and um pass some manifest and what happens right you press enter what happens that's the question and we are all in that interview situation now so we want to talk about the interesting bits of the API server and Q cuttle what happens if we do that and um not everything is new so there was a old talk from Daniel Smith years ago many years ago I'm not sure maybe eight years ago or so with a similar title but of course cube has changed um has become much more complex and I bet um 80% of the audience um has joined the the project after that talk.

So will be lots of new stuff. Anyway, this is a um the start of the conversation here and um most of you will done have done minus minus v something like 7 8 9 something this dimension and you get logging right so you see the the cube cutle does something and um in particular it's doing this request right the request here and this looks super innocent um you find the batch the word batch the word v1 and on the first view you you see job right but there's the first detail which is super interesting. This is jobs lowerase plural and this one is an uppercase word singular and this is already not trivial in Kubernetes um how this mapping actually happens and of course um when the request is done it's a post request to a URL and there's a uh returned and this means success so a batch is created but everything in between we want to talk through now so um this mapping um you will have heard about kinds and resources in kubernetes And um the kind is the one in the manifest. Resource is the one in the in the API path here.

Um they look different um but they don't have to be um similar. They can be completely different word uh words. And for exa
