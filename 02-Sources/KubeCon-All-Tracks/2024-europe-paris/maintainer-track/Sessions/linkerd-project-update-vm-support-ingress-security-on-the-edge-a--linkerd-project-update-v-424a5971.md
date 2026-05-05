---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Networking", "Community Governance"]
speakers: ["William Morgan", "David McLaughlin", "Buoyant"]
sched_url: https://kccnceu2024.sched.com/event/1Yhfu/linkerd-project-update-vm-support-ingress-security-on-the-edge-and-rust-william-morgan-david-mclaughlin-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Linkerd+Project+Update%3A+VM+Support%2C+Ingress%2C+Security+on+the+Edge%2C+and+Rust+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Linkerd Project Update: VM Support, Ingress, Security on the Edge, and Rust - William Morgan & David McLaughlin, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: William Morgan, David McLaughlin, Buoyant
- Schedule: https://kccnceu2024.sched.com/event/1Yhfu/linkerd-project-update-vm-support-ingress-security-on-the-edge-and-rust-william-morgan-david-mclaughlin-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Linkerd+Project+Update%3A+VM+Support%2C+Ingress%2C+Security+on+the+Edge%2C+and+Rust+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Linkerd Project Update: VM Support, Ingress, Security on the Edge, and Rust.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhfu/linkerd-project-update-vm-support-ingress-security-on-the-edge-and-rust-william-morgan-david-mclaughlin-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Linkerd+Project+Update%3A+VM+Support%2C+Ingress%2C+Security+on+the+Edge%2C+and+Rust+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N76X9N_y7j8
- YouTube title: Linkerd Project Update: VM Support, Ingress, Security on the Edge, and Rust
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/linkerd-project-update-vm-support-ingress-security-on-the-edge-and-rus/N76X9N_y7j8.txt
- Transcript chars: 32522
- Keywords: cluster, linker, traffic, linkerd, mesh, control, gateway, release, little, proxies, support, called, another, whatever, component, ingress, security, pretty

### Resumo baseado na transcript

hi everyone uh I'm William Morgan I have an official title these days I used to be the person who speaks a lot about linkerd now I have an official role in the project which is called director uh so I'm in a officially in a markdown file in a GitHub repo with that um so thank you all for coming today this is our cucon uh EU project update talk I'm going to try and keep this you know pretty uh high level and pretty informal so um you observable Cloud native platform Now link is pretty kubernetes specific so if you're not using kubernetes this can't really do its job but if you are then this is how I think of you know kind of what we're trying to to to provide to you we want to give you the ability to build a platform and you know to build it on top of kubernetes that has those three properties right secure reliable observable linger is not a complete solution we can't fix every security aspect you know 16 so that's uh you know the way it works today is Linker will happily route any traffic that you want outside of the um outside of the cluster um it doesn't give you great metrics for that traffic for kind of maybe not ideal reasons um and it doesn't really give you great control over that traffic either so both of those things end up being really important um you know especially in security conscious environments so we're going to uh we're going to fix that we're going to

### Excerpt da transcript

hi everyone uh I'm William Morgan I have an official title these days I used to be the person who speaks a lot about linkerd now I have an official role in the project which is called director uh so I'm in a officially in a markdown file in a GitHub repo with that um so thank you all for coming today this is our cucon uh EU project update talk I'm going to try and keep this you know pretty uh high level and pretty informal so um you you know and probably there'll be lots of space for questions at the end so feel free to come up afterwards um and if I don't get a chance to answer your questions myself and then a bunch of the Linker maintainers are hanging out at the project Pavilion the cncf project Pavilion there's a Linker booth there so please come say hi to us we'd love to talk to you um all right so i' you know I've I've titled this talk and I think the title has changed a little bit um since what's officially on the schedule uh I'm going to talk about VM support I'm going to talk about egress I'm going to talk about spiffy and then I'm going to talk about more so so uh hopefully this is what you were expecting let's go ahead and get started uh I've got I'm going to warn you I've got two or three slides in here that we've been using for probably eight years so and one day we're going to you know sometimes we'll update the numbers and stuff one day we'll give these another bit of Polish but you know just imagine a bunch of uh baguer open- Source nerds you know frantically trying to put slides together at the very last minute definitely not what happened in this talk but you can imagine that you know is happening maybe for some of these other talks uh so what is linkerd it's a service mesh uh I do have one slide about what a service mesh is so don't worry if if You' never heard that term before get ready for you know a thrilling Journey uh created originally by a company called buoyant eight plus years in production you know almost 10,000 slack channel members so if you have a moment to go to slack.

linkerd doio and you don't have to say anything just log in that'd be great because I'd love to get that finally to to 10,000 people in that in that slack um lots of GitHub stars and contributors and and and things like that and we've been a a cncf project since almost the beginning of the cncf I think we we joined in 2016 as the fifth project uh and we joined as a uh they didn't have incubation back then they called it Inception so we joined as an Inception
