---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Cloud Native Novice"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Doug Smith", "Surya Seetharaman", "Red Hat", "Shane Utt", "Kong", "Lior Lieberman", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7oD/solving-the-kubernetes-networking-api-rubiks-cube-doug-smith-surya-seetharaman-red-hat-shane-utt-kong-lior-lieberman-google
youtube_search_url: https://www.youtube.com/results?search_query=Solving+the+Kubernetes+Networking+API+Rubik%27s+Cube+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Solving the Kubernetes Networking API Rubik's Cube - Doug Smith & Surya Seetharaman, Red Hat; Shane Utt, Kong; Lior Lieberman, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Doug Smith, Surya Seetharaman, Red Hat, Shane Utt, Kong, Lior Lieberman, Google
- Schedule: https://kccncna2024.sched.com/event/1i7oD/solving-the-kubernetes-networking-api-rubiks-cube-doug-smith-surya-seetharaman-red-hat-shane-utt-kong-lior-lieberman-google
- Busca YouTube: https://www.youtube.com/results?search_query=Solving+the+Kubernetes+Networking+API+Rubik%27s+Cube+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Solving the Kubernetes Networking API Rubik's Cube.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oD/solving-the-kubernetes-networking-api-rubiks-cube-doug-smith-surya-seetharaman-red-hat-shane-utt-kong-lior-lieberman-google
- YouTube search: https://www.youtube.com/results?search_query=Solving+the+Kubernetes+Networking+API+Rubik%27s+Cube+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=S5QsqEb8wec
- YouTube title: Solving the Kubernetes Networking API Rubik's Cube - D. Smith, S. Seetharaman, S. Utt, L. Lieberman
- Match score: 0.79
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/solving-the-kubernetes-networking-api-rubiks-cube/S5QsqEb8wec.txt
- Transcript chars: 29515
- Keywords: network, networking, working, request, question, networks, gateway, resource, workloads, adapter, multiple, device, loaded, resources, actually, basically, specific, attach

### Resumo baseado na transcript

welcome to solving the kubernetes networking API Rubik's Cube hey yeah so I'm Leo liberman I'm s reability engineer at Google uh mostly active in the gway API community and I'm I'm iner of a small tool called Ingress to getaway uh which helps people migrate Ingress uh configurations to gway API hi my name is Doug Smith I am an engineer at red hat and I am involved in the network Plumbing working group as well as uh cni the container network interface hey everyone my name is suran

### Excerpt da transcript

welcome to solving the kubernetes networking API Rubik's Cube hey yeah so I'm Leo liberman I'm s reability engineer at Google uh mostly active in the gway API community and I'm I'm iner of a small tool called Ingress to getaway uh which helps people migrate Ingress uh configurations to gway API hi my name is Doug Smith I am an engineer at red hat and I am involved in the network Plumbing working group as well as uh cni the container network interface hey everyone my name is suran I'm an engineer working at Red Hat on open shift networking I contribute to Sig Network mostly in the network policy area so very happy to be here at kipcon with all of you and I'm Shane uh I'm an engineer at red hat with both Doug and sua and I work with leor on Gateway API and Upstream I'm also a Sig Network chair and a maintainer of Gateway API just to get a read of the room a little bit um raise your hand if you're here because you already do quite a bit with kubernetes networking okay raise your hand if you're here because of AIML workloads interesting raise your hand if you're here and you're completely new to all of it and you're like just interested in whatever is going on here networking okay and that is the majority okay cool so we'll start by just giving an overview of Sig Network um sub projects and working groups and some of the things that connect to Sig Network that aren't exactly under it so there's a lot of sub projects in Sig Network it's a particularly busy Sig uh here's a sample of some of those Gateway API Network policy and multi Network you may have heard of there's a lot more and if you're interested in seeing the breadth of it hit that QR code and it takes you to our readme where you can see everything that we have under our purview outside of those things we we also connect with the container network interface cni Doug works on that um which is the standard for configuring network interfaces for containers it's how Network providers plug into kubernetes we also have the Kates Network Plumbing working group which we kind of put wanted to put a special mention here this is where you might see things like malus and stuff like that show up quite a bit um and more lately or more uh more recently the working group serving and device management working groups which are mostly focused on things related to I workloads have been having intersections with networking which we're going to talk about including the llm instance Gateway and the device management working
