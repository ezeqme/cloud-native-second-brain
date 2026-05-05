---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Andrew Martin", "ControlPlane"]
sched_url: https://kccnceu2022.sched.com/event/ytre/a-treasure-map-of-hacking-and-defending-kubernetes-andrew-martin-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=A+Treasure+Map+of+Hacking+%28and+Defending%29+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# A Treasure Map of Hacking (and Defending) Kubernetes - Andrew Martin, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Andrew Martin, ControlPlane
- Schedule: https://kccnceu2022.sched.com/event/ytre/a-treasure-map-of-hacking-and-defending-kubernetes-andrew-martin-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=A+Treasure+Map+of+Hacking+%28and+Defending%29+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre A Treasure Map of Hacking (and Defending) Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytre/a-treasure-map-of-hacking-and-defending-kubernetes-andrew-martin-controlplane
- YouTube search: https://www.youtube.com/results?search_query=A+Treasure+Map+of+Hacking+%28and+Defending%29+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1HbwfpE4XKY
- YouTube title: A Treasure Map of Hacking (and Defending) Kubernetes - Andrew Martin, ControlPlane
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/a-treasure-map-of-hacking-and-defending-kubernetes/1HbwfpE4XKY.txt
- Transcript chars: 31275
- Keywords: container, security, reverse, everything, attack, running, process, kernel, supply, inside, version, public, exploit, another, course, source, potentially, malicious

### Resumo baseado na transcript

okay hello and welcome to that there's still space incidentally there's probably another 20 seats if you want to let a few more people in okay we'll see how we go hello and welcome thank you very much for coming to this talk this is one of the most packed rooms i've ever delivered to really appreciate you attending when there's so many other high quality talks going on in this slot thank you i will do my best to complete everything in 35 minutes so i am andy i'm okay so what we are about to see is and npm supply chain attack uh that's not it wowzers okay we are there so all right i think maybe possibly this will work the demo gods man i feel they crucified me this time all

### Excerpt da transcript

okay hello and welcome to that there's still space incidentally there's probably another 20 seats if you want to let a few more people in okay we'll see how we go hello and welcome thank you very much for coming to this talk this is one of the most packed rooms i've ever delivered to really appreciate you attending when there's so many other high quality talks going on in this slot thank you i will do my best to complete everything in 35 minutes so i am andy i'm ceo at control plane we do cloud native security engineering we're very heavily invested in training the community work in tag security and everything to do with cncf open sf open source very proud advocates i have done various things i've written a book which you will hear a little bit about today uh there is a sans course involved my excellent colleagues also participate in a lot of training and we'll see links to those things too and this is my pre-eminent co-author mr michael hassenblast solutions architect at aws and together we wrote to the book hacking kubernetes it is available as a free download the first half as a pdf on the control plane website and i will give you a whistle stop tour of what we have inside it so what will we talk about today well it's just a lot of demos and i will do my best to ensure they all work i'm wired in the demo gods at least don't have the ethereal wi-fi to contend with so we'll start off looking at how the supply chain gets us into a cluster we will look at what to do once we're inside a cluster we'll demo a container breakouts by kernel exploitation in the dirty pipe and we will look at how to take over a cloud account there is so much prior art in this space thank you to everybody who has participated open sourced spoken written about these things we stand on the shoulders of giants and these are just a few of the luminaries who have inspired me and my colleagues to go on this journey so what happens when kubernetes gets deployed the security team normally panic and that's because somebody like captain hash jack is all up in their clusters captain hashtag is our eight bit adversary we're going to threat model and attack on these clusters this is the person who we're terrified of in this instance but this this talk is called a treasure map why is there a treasure map involved well this is because from the inside of a pod this is what you might want to look at to try and break out this is a guide to how we manually pen test pods it's the microcosm of linux in
