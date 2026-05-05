---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Mattia Lavacca", "Kong", "Gaurav Ghildiyal", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7s2/with-great-flexibility-comes-great-complexity-inspect-your-gateway-api-configuration-mattia-lavacca-kong-gaurav-ghildiyal-google
youtube_search_url: https://www.youtube.com/results?search_query=With+Great+Flexibility+Comes+Great+Complexity%3A+Inspect+Your+Gateway+API+Configuration+CNCF+KubeCon+2024
slides: []
status: parsed
---

# With Great Flexibility Comes Great Complexity: Inspect Your Gateway API Configuration - Mattia Lavacca, Kong & Gaurav Ghildiyal, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: Mattia Lavacca, Kong, Gaurav Ghildiyal, Google
- Schedule: https://kccncna2024.sched.com/event/1i7s2/with-great-flexibility-comes-great-complexity-inspect-your-gateway-api-configuration-mattia-lavacca-kong-gaurav-ghildiyal-google
- Busca YouTube: https://www.youtube.com/results?search_query=With+Great+Flexibility+Comes+Great+Complexity%3A+Inspect+Your+Gateway+API+Configuration+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre With Great Flexibility Comes Great Complexity: Inspect Your Gateway API Configuration.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7s2/with-great-flexibility-comes-great-complexity-inspect-your-gateway-api-configuration-mattia-lavacca-kong-gaurav-ghildiyal-google
- YouTube search: https://www.youtube.com/results?search_query=With+Great+Flexibility+Comes+Great+Complexity%3A+Inspect+Your+Gateway+API+Configuration+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kbTVzAhtHKs
- YouTube title: With Great Flexibility Comes Great Complexity: Inspect Your Gateway API... M. Lavacca, G. Ghildiyal
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/with-great-flexibility-comes-great-complexity-inspect-your-gateway-api/kbTVzAhtHKs.txt
- Transcript chars: 23020
- Keywords: gateway, policies, resources, actually, policy, ingress, specific, another, resource, multiple, reference, figure, routes, describe, effective, create, basically, complexity

### Resumo baseado na transcript

uh hello everyone and welcome uh this is one of the final presentations of this cubec Con and I and I really hope you all are not too tired well at least I am tired but I hope we can make it worthwhile for you this session is going to be about inspecting your gateway API configuration my name is gorov and I'm a software engineer at Google where I work in the GK networking team I am also an active contributor to the Gateway API project and and a is not that much because it's great it has been designed very well but because of all that um flexibility you get a lot of complexity right this is an example uh this is a graph of the interaction between the multiple modules of the

### Excerpt da transcript

uh hello everyone and welcome uh this is one of the final presentations of this cubec Con and I and I really hope you all are not too tired well at least I am tired but I hope we can make it worthwhile for you this session is going to be about inspecting your gateway API configuration my name is gorov and I'm a software engineer at Google where I work in the GK networking team I am also an active contributor to the Gateway API project and and a maintainer of Gateway cutle yeah hi everybody I'm mataka and I'm a software engineer working at Kong and I'm a gatei maintainer so uh our main aim with today's presentation is to empower you all with the tools and knowledge that you need to easily work with the Gateway API how we going to be going about doing that is we'll be setting up the stage for example we'll start out with giving you a background about what the precursor of KP API looked like yes I'm talking about our very own Ingress API we'll be discussing what the limitations of the Ingress API were and then we'll be moving on to how kateway API solves most or almost all of those limitations after that we'll be doing a deep dip of all the complexities or all the challenges that you may run into while working with the Gateway API and look at possible solutions on how you can overcome those challenges so yeah let's get started with the with the Ingress I guess that all of you already know about Ingress what is ingress what's well it's it's a very well-known API and very widely used API right so Ingress it's very well used and it's simple because it's a kubernetes COR API which means that if you create a new kubernetes cluster you have your Ingress API there just ready to be used and it's also simple you can just create an Ingress resource you well of course you you need to have an Ingress class uh installed in your cluster but you just create an Ingress and everything works of course you also need to have an Ingress implementation installed in your cluster but there are some downsides with Ingress the first one was the lack of core features so basically when Ingress has been designed um the feature set wasn't completed uh so wasn't complete and this led to the creation of custom extensions everywhere uh a lot of annotations implementation specific annotations and this led to the lack of portability so basically if you had an Ingress configuration an Ingress based configuration um for a specific implementation it was very hard and complex to m grade to using a
