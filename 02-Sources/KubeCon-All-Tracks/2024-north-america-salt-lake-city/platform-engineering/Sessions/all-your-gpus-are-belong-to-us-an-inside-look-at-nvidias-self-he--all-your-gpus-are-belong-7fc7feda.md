---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Ryan Hallisey", "Piotr Prokop PL", "NVIDIA"]
sched_url: https://kccncna2024.sched.com/event/1i7kJ/all-your-gpus-are-belong-to-us-an-inside-look-at-nvidias-self-healing-geforce-now-infrastructure-ryan-hallisey-piotr-prokop-pl-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=All-Your-GPUs-Are-Belong-to-Us%3A+An+Inside+Look+at+NVIDIA%27s+Self-Healing+GeForce+NOW+Infrastructure+CNCF+KubeCon+2024
slides: []
status: parsed
---

# All-Your-GPUs-Are-Belong-to-Us: An Inside Look at NVIDIA's Self-Healing GeForce NOW Infrastructure - Ryan Hallisey & Piotr Prokop PL, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United States / Salt Lake City
- Speakers: Ryan Hallisey, Piotr Prokop PL, NVIDIA
- Schedule: https://kccncna2024.sched.com/event/1i7kJ/all-your-gpus-are-belong-to-us-an-inside-look-at-nvidias-self-healing-geforce-now-infrastructure-ryan-hallisey-piotr-prokop-pl-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=All-Your-GPUs-Are-Belong-to-Us%3A+An+Inside+Look+at+NVIDIA%27s+Self-Healing+GeForce+NOW+Infrastructure+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre All-Your-GPUs-Are-Belong-to-Us: An Inside Look at NVIDIA's Self-Healing GeForce NOW Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kJ/all-your-gpus-are-belong-to-us-an-inside-look-at-nvidias-self-healing-geforce-now-infrastructure-ryan-hallisey-piotr-prokop-pl-nvidia
- YouTube search: https://www.youtube.com/results?search_query=All-Your-GPUs-Are-Belong-to-Us%3A+An+Inside+Look+at+NVIDIA%27s+Self-Healing+GeForce+NOW+Infrastructure+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iLnHtKwmu2I
- YouTube title: All-Your-GPUs-Are-Belong-to-Us: An Inside Look at NVIDIA's Self-Healin... R. Hallisey & P. Prokop PL
- Match score: 0.85
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/all-your-gpus-are-belong-to-us-an-inside-look-at-nvidias-self-healing/iLnHtKwmu2I.txt
- Transcript chars: 38456
- Keywords: maintenance, actually, important, workloads, probably, remediation, centers, gpu, wanted, states, second, upgrade, cluster, solution, notify, infrastructure, define, center

### Resumo baseado na transcript

uh this is all your gpus are belong to us I'm Ryan hesy and this is p procop we work at Nvidia and we're going to be talking about how we maintain GeForce now the GeForce now infrastructure okay so if you don't know about uh GeForce now if you're not familiar with it um little intro to it um but we do uh at Nvidia with gForce now we have a a service where we offer you to play games in the cloud and we can stream it to

### Excerpt da transcript

uh this is all your gpus are belong to us I'm Ryan hesy and this is p procop we work at Nvidia and we're going to be talking about how we maintain GeForce now the GeForce now infrastructure okay so if you don't know about uh GeForce now if you're not familiar with it um little intro to it um but we do uh at Nvidia with gForce now we have a a service where we offer you to play games in the cloud and we can stream it to your device and so what what uh how does this look with infrastructure so we take gpus we put them in our data centers and you as an end user can open up your device you can go to the GeForce now client and open up your steam Library start playing your game and the graphics for that game will be will be rendered on a GPU in the cloud and those Graphics get streamed back over the network to your device so that's a little bit how it works um these these data centers these these clusters we um our Fleet is is a bunch of it's all it's all kubernetes or mostly kubernetes the one we're going to be talking about is uh we have about 40 plus kubernetes clusters that we run which about 30,000 plus nodes might even be more than that now um and we run a lot of these workloads uh in VMS so we use CT a lot lot uh these These workloads are uh Windows guests and we um so makes so we run Windows guest we attach gpus to them and you know we we render graphics and and stream them to and users and we're about 60,000 plus gpus across our data centers uh geolocated all over the world okay um so what's our philosophy when when I say maintaining the fleet like doing maintenance what's our philosophy um at Nvidia so I'm going to give you an analogy if if you need two requirements if you wanted to build a race car first requirement is you really want to build a fast car right the second requirement is you need to be able to do and repair your car on the racetrack the second requirement is equally as important as the first and so with kubernetes in production it's really important that we keep that in mind that we run a really good service we run a service that's always available for us and one that we can repair while it's run while it's in production okay so what does that mean like maintaining the fleet like what are all the steps the things that we do when we want to maintain this infrastructure well we do a ton of things um we always want to make sure our gpus are up to date right there's new gpus that are coming out all the time and we have we want to get them in
