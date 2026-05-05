---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Operations"
themes: ["Kubernetes Core"]
speakers: ["Kevin Ward", "ControlPlane"]
sched_url: https://kccnceu2022.sched.com/event/ytpr/tweezering-kubernetes-resources-operating-on-operators-kevin-ward-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Tweezering+Kubernetes+Resources%3A+Operating+on+Operators+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Tweezering Kubernetes Resources: Operating on Operators - Kevin Ward, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Operations]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Kevin Ward, ControlPlane
- Schedule: https://kccnceu2022.sched.com/event/ytpr/tweezering-kubernetes-resources-operating-on-operators-kevin-ward-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Tweezering+Kubernetes+Resources%3A+Operating+on+Operators+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Tweezering Kubernetes Resources: Operating on Operators.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpr/tweezering-kubernetes-resources-operating-on-operators-kevin-ward-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Tweezering+Kubernetes+Resources%3A+Operating+on+Operators+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dcKAr8UNgMQ
- YouTube title: Tweezering Kubernetes Resources: Operating on Operators - Kevin Ward, ControlPlane
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/tweezering-kubernetes-resources-operating-on-operators/dcKAr8UNgMQ.txt
- Transcript chars: 35547
- Keywords: operator, cluster, security, operators, permissions, resources, access, whether, essentially, actually, basically, deployed, within, little, custom, container, supposed, potentially

### Resumo baseado na transcript

welcome to my talk today this is tweezing kubernetes resources operating on operators so what we're going to talk about today um primarily kubernetes operator security um i'm going to briefly go over a little bit about kubernetes operators talk about security i'm also going to talk about what does the operator introduce into kubernetes um how can that be abused by an attacker and also how can i now review that from a security perspective to see whether there's any kind of risks associated with it and then lastly

### Excerpt da transcript

welcome to my talk today this is tweezing kubernetes resources operating on operators so what we're going to talk about today um primarily kubernetes operator security um i'm going to briefly go over a little bit about kubernetes operators talk about security i'm also going to talk about what does the operator introduce into kubernetes um how can that be abused by an attacker and also how can i now review that from a security perspective to see whether there's any kind of risks associated with it and then lastly um how can i detect operator abuse so i'm kevin ward i'm from control plane i'm a senior security engineer i've got over a decade of experience working in the security domain doing all sorts of things from threat modeling to security architecture i have also do pen testing where i can my mantra is i like to harden by day because primarily i'm working on securing stuff and then by night i like to sit in the dark and hack stuff and see how i can exploit it so essentially kubernetes operator is an extension of the kubernetes api with some operational knowledge that operational knowledge is provided by custom resource definitions which extend the capabilities of kubernetes beyond its initial primitives there's a controller that reconciles those resources for you um utilizing all the magic that kubernetes has these are primarily used or often a use case for it is stateful resolution so you might have a database that you wish to update you may want to drain the data out of it you may want to rehydrate it this is usually a very good pattern to try and keeping it in sync with your cluster there are some operator tools that exist out there primarily through the operator framework which offers several little things that you can do the operator sdk provides a scaffold which automatically generates code for you and you can bootstrap a project really nice and fast so it's super useful for developers the operator lifecycle manager essentially installs updates and manages your operator for your cluster it does so via an operator bundle which consists of a cluster service version which contains everything that an operator needs pretty much all bundled up by a little bit of custom resource definitions interestingly enough the actual olm it consists of two operators in itself so there's an it's an olm operator and there's also a catalog operator last on the list is operator hub which is essentially a just a community hub where you can submit and share your operators
