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
themes: ["AI ML", "Community Governance"]
speakers: ["Sunjay Bhatia", "VMware", "Nigel Brown", "Intuit"]
sched_url: https://kccncna2023.sched.com/event/1R2uw/contour-project-update-highlighting-new-features-and-community-contributions-sunjay-bhatia-vmware-nigel-brown-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Contour+Project+Update%3A+Highlighting+New+Features+and+Community+Contributions+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Contour Project Update: Highlighting New Features and Community Contributions - Sunjay Bhatia, VMware & Nigel Brown, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Sunjay Bhatia, VMware, Nigel Brown, Intuit
- Schedule: https://kccncna2023.sched.com/event/1R2uw/contour-project-update-highlighting-new-features-and-community-contributions-sunjay-bhatia-vmware-nigel-brown-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Contour+Project+Update%3A+Highlighting+New+Features+and+Community+Contributions+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Contour Project Update: Highlighting New Features and Community Contributions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2uw/contour-project-update-highlighting-new-features-and-community-contributions-sunjay-bhatia-vmware-nigel-brown-intuit
- YouTube search: https://www.youtube.com/results?search_query=Contour+Project+Update%3A+Highlighting+New+Features+and+Community+Contributions+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=X1wL8CLbIzc
- YouTube title: Contour Project Update: Highlighting New Features and Community Contr... Sunjay Bhatia & Nigel Brown
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/contour-project-update-highlighting-new-features-and-community-contrib/X1wL8CLbIzc.txt
- Transcript chars: 21703
- Keywords: contour, gateway, features, envoy, support, release, little, ingress, feature, production, wanted, contributors, github, interested, contributions, around, configuration, traffic

### Resumo baseado na transcript

welcome to the uh Contour project update uh we're going to be talking about uh project Contour what's been happening recently and uh particularly highlighting some of the really great uh Community contributions that we've had lately so let's get started uh my name is Sanjay baa I'm one of the uh uh maintainers of Contour I'm a engineer at Vare and here we have yeah my name is Nigel I am a developer Advocate at Inuit and I FOC focus on community things around Contour all right so let's

### Excerpt da transcript

welcome to the uh Contour project update uh we're going to be talking about uh project Contour what's been happening recently and uh particularly highlighting some of the really great uh Community contributions that we've had lately so let's get started uh my name is Sanjay baa I'm one of the uh uh maintainers of Contour I'm a engineer at Vare and here we have yeah my name is Nigel I am a developer Advocate at Inuit and I FOC focus on community things around Contour all right so let's get started off with uh just a little bit of background just for anyone who's who's new to this space um so what is Contour uh Contour is a kubernetes Ingress controller that uh uses Envoy um if we're kind of not super familiar with Contour or not familiar with Ingress controls in general here's a little diagram about generally how Contour is set up in a in a kubernetes cluster so um uh we read configuration from kubernetes resources uh Envoy and Contour are set up to securely communicate over the uh XDS protocol um and uh your CL typically web clients can be other types of traffic as well connect to a a single IP address and for the uh to get access to your backend Services typically using a service of type load balancer um and then the configuration that Contour sends to Envoy uh routes traffic to your um uh apps based on different paths different host names um and and yeah um onvo is uh I'm sure people have seen in uh various talks and Envoy con here at at uh at cucon on Monday but uh Envoy is uh uh a super powerful tool it's kind of become like a deao standard for like proxying and surface proxying in kubernetes especially um so uh here's some reasons I guess why uh we use Envoy as a data plane um super well-maintained uh well tested performant observable uh proxy that uh we're like it has been the Contour has been built around since the it its Inception and we're super happy to be involved with the envoy community and uh build a product around it yeah yeah uh another reason that Contour is a great tool to use is that it's not really a new project and and it's uh something that is being used in production scale at VMware and other companies um it's been an incubating project since 2020 um and it's got a robust feature set around it and active maintainers to help uh Drive the project forward uh so a little bit about the history uh the first uh instance of Contour back in 2017 um and as we've gone through time uh we the Gateway API conformance was a big moment for us in Jul
