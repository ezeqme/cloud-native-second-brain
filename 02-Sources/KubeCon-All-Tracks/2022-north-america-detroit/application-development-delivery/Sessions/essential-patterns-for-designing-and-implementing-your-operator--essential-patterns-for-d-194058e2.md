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
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Michael Hrivnak", "Austin Macdonald", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182Dc/essential-patterns-for-designing-and-implementing-your-operator-michael-hrivnak-austin-macdonald-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Essential+Patterns+For+Designing+And+Implementing+Your+Operator+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Essential Patterns For Designing And Implementing Your Operator - Michael Hrivnak & Austin Macdonald, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Application + Development + Delivery]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Michael Hrivnak, Austin Macdonald, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182Dc/essential-patterns-for-designing-and-implementing-your-operator-michael-hrivnak-austin-macdonald-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Essential+Patterns+For+Designing+And+Implementing+Your+Operator+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Essential Patterns For Designing And Implementing Your Operator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Dc/essential-patterns-for-designing-and-implementing-your-operator-michael-hrivnak-austin-macdonald-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Essential+Patterns+For+Designing+And+Implementing+Your+Operator+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_SCzRtU5RRA
- YouTube title: Essential Patterns For Designing And Implementing Your Operator - Michael Hrivnak & Austin Macdonald
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/essential-patterns-for-designing-and-implementing-your-operator/_SCzRtU5RRA.txt
- Transcript chars: 32349
- Keywords: operator, cluster, clusters, resource, client, operators, controller, reconcile, config, runtime, feature, resources, events, server, another, access, course, native

### Resumo baseado na transcript

thank you welcome come on in there's a lot more room down on the far end of uh this big wide space uh so come spread out make yourself at home uh we're just thrilled to be here I'm Michael this is my colleague Austin uh we work on the operator framework and now and in the past in various capacities we're here to share some lessons that we've learned with you about operator design we're going to tag team here a little bit I'm going to dive in and

### Excerpt da transcript

thank you welcome come on in there's a lot more room down on the far end of uh this big wide space uh so come spread out make yourself at home uh we're just thrilled to be here I'm Michael this is my colleague Austin uh we work on the operator framework and now and in the past in various capacities we're here to share some lessons that we've learned with you about operator design we're going to tag team here a little bit I'm going to dive in and I think Austin's going to be back in a few minutes let's get right to it getting started with operators in operator development is pretty easy these days these days we've got the operator SDK there's other tooling out there there's Cube Builder a variety of languages are supported now that you can use for developing some kind of operator and you can get something up and going pretty quick that does installation on installation maybe a little bit of reconfiguration and be pretty satisfied with that but we want you to have more advanced more useful operators that you can really do things with that really make day two operations successful in day two as we've learned is full of messy challenges these are just you know the first 20 or so that came to mind uh that you can face when you're orchestrating operational concerns with your operator really solving operational problems what kind of things SRE teams worry about so we have a lot of experience managing stateful infrastructure and that comes with a lot of those day two challenges um you know things like uh you know bare metal server provisioning and these kinds of things we've helped make operators for cluster installation cluster upgrade a lot of infrastructure related stuff that can take time it can be error prone it can be very configuration sensitive uh when you have a cloud API of course you know what you're going to get in advance for example when you're deploying a cluster when you're doing that in a data center there's a lot more opportunity for for variation of environment right so we've we've done a lot of that and uh made a lot of these kind of operators in that space and yes we've even made an operator for installing more operators if only it was so easy as as this uh this is my Fogo I hope you'll be okay with some of that along the way uh if we could reconcile and just say what's the current state what's the desired state do a little bit of work to move the one a little closer to the other and then set some status and we're out of there success that wou
