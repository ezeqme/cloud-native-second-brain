---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Alex Meijer", "Michael Dresser", "Stackwatch"]
sched_url: https://kccncna2023.sched.com/event/1R2so/node-size-matters-running-k8s-as-cheaply-as-possible-alex-meijer-michael-dresser-stackwatch
youtube_search_url: https://www.youtube.com/results?search_query=Node+Size+Matters+-+Running+K8s+as+Cheaply+as+Possible+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Node Size Matters - Running K8s as Cheaply as Possible - Alex Meijer & Michael Dresser, Stackwatch

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Alex Meijer, Michael Dresser, Stackwatch
- Schedule: https://kccncna2023.sched.com/event/1R2so/node-size-matters-running-k8s-as-cheaply-as-possible-alex-meijer-michael-dresser-stackwatch
- Busca YouTube: https://www.youtube.com/results?search_query=Node+Size+Matters+-+Running+K8s+as+Cheaply+as+Possible+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Node Size Matters - Running K8s as Cheaply as Possible.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2so/node-size-matters-running-k8s-as-cheaply-as-possible-alex-meijer-michael-dresser-stackwatch
- YouTube search: https://www.youtube.com/results?search_query=Node+Size+Matters+-+Running+K8s+as+Cheaply+as+Possible+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6vNI_O6sdvY
- YouTube title: Node Size Matters - Running K8s as Cheaply as Possible - Alex Meijer & Michael Dresser, Stackwatch
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/node-size-matters-running-k8s-as-cheaply-as-possible/6vNI_O6sdvY.txt
- Transcript chars: 45448
- Keywords: overhead, cost, capacity, allocatable, instance, interesting, memory, running, algorithm, itself, amount, cluster, information, workloads, available, workload, family, larger

### Resumo baseado na transcript

hi everyone good evening uh my name is Alex Meyer I'm Michael dresser and we're software engineers at Cube cost uh we we're the creators of the Cube cost app and also uh open cost and we're super excited to share uh some interesting information we found with you tonight uh in the course of you know developing our app right uh surface and cost information for customers and helping them act on that to you know size their nodes and workloads so we'll do a quick overview of what

### Excerpt da transcript

hi everyone good evening uh my name is Alex Meyer I'm Michael dresser and we're software engineers at Cube cost uh we we're the creators of the Cube cost app and also uh open cost and we're super excited to share uh some interesting information we found with you tonight uh in the course of you know developing our app right uh surface and cost information for customers and helping them act on that to you know size their nodes and workloads so we'll do a quick overview of what we're going to go over tonight we'll start by defining this concept of node overhead or we'll shorten it to overhead we'll go over what it is how do you you know obtain it right how it's calculated uh we'll go over open cost very quickly um which is the open source component of Cube cost uh we'll have a quick demo of how to use open cost to determine these concepts of node overhead and sort of measure your sunk cost if you will uh we'll then use this tooling to conduct a study and share the results of that study with you and we'll summarize of our key findings from that um in the interest of you know giving action items based on the study information we'll go over some node sizing algorithms uh both our existing node sizing algorithm and then we'll compare and contrast that to the updated node sizing algorithm that sort of incorporates these ideas uh of node overhead so to start right off uh if we Define node overhead it's basically compute that is used to run kubernetes itself right the cost of doing business if you will so um nodes typically have capacity I'm sure we're all familiar with that right that's the sticker price that's what you're built for uh in gcp or you know AWS or whatever you're using um it's what's in the pricing apis and U that's what you what you're paying for essentially right now there is some subset of that that is defined as allocatable now allocatable capacity is something that's passed to the cuet through the command line arguments when it's booted up so we're going to study a little bit both of a property of kubernetes itself but also managed kubernetes right um the difference between these is is overheads so overhead includes things like the cuet right uh any control plane infrastructure running on that node if it's applicable um the container run time like Docker or container D itself um in general any software running directly on the Node that isn't in a pot right uh overhead does not include things like Prometheus um any sort of DNS pods or you know C m
