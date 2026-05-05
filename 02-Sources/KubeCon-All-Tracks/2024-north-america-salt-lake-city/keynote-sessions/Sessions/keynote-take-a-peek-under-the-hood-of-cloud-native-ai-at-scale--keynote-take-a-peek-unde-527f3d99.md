---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Keynote Sessions"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Chen Goldberg", "Senior Vice President of Engineering", "CoreWeave", "Peter Salanki", "Chief Technology Officer", "CoreWeave"]
sched_url: https://kccncna2024.sched.com/event/1noNg/keynote-take-a-peek-under-the-hood-of-cloud-native-ai-at-scale-chen-goldberg-senior-vice-president-of-engineering-coreweave-peter-salanki-chief-technology-officer-coreweave
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Take+a+Peek+Under+the+Hood+of+Cloud-Native+AI+at+Scale+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Keynote: Take a Peek Under the Hood of Cloud-Native AI at Scale - Chen Goldberg, Senior Vice President of Engineering, CoreWeave & Peter Salanki, Chief Technology Officer, CoreWeave

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Chen Goldberg, Senior Vice President of Engineering, CoreWeave, Peter Salanki, Chief Technology Officer, CoreWeave
- Schedule: https://kccncna2024.sched.com/event/1noNg/keynote-take-a-peek-under-the-hood-of-cloud-native-ai-at-scale-chen-goldberg-senior-vice-president-of-engineering-coreweave-peter-salanki-chief-technology-officer-coreweave
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Take+a+Peek+Under+the+Hood+of+Cloud-Native+AI+at+Scale+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Keynote: Take a Peek Under the Hood of Cloud-Native AI at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1noNg/keynote-take-a-peek-under-the-hood-of-cloud-native-ai-at-scale-chen-goldberg-senior-vice-president-of-engineering-coreweave-peter-salanki-chief-technology-officer-coreweave
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Take+a+Peek+Under+the+Hood+of+Cloud-Native+AI+at+Scale+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FvLvPiQ6zBc
- YouTube title: Keynote: Take a Peek Under the Hood of Cloud-Native AI at Scale - Chen Goldberg & Peter Salanki
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/keynote-take-a-peek-under-the-hood-of-cloud-native-ai-at-scale/FvLvPiQ6zBc.txt
- Transcript chars: 14090
- Keywords: cluster, training, running, clusters, performance, possible, metrics, health, gpu, hardware, interruptions, management, manage, production, technologies, customers, platform, components

### Resumo baseado na transcript

it's so great to be here H I'm Ken Goldberg SVP of engineering at kwe I'm Peter slanky I'm the cor CTO if you don't know who corv is we're the AI hyperscaler we bring the latest Technologies to AI Enterprises all over the world faster and more reliable than anyone else in the last decade we have seen an explosion of workloads running on kubernetes from e-commerce platforms to gaming sers web application and databases now it's the AI era at Cove we decided to take advantage of kubernetes

### Excerpt da transcript

it's so great to be here H I'm Ken Goldberg SVP of engineering at kwe I'm Peter slanky I'm the cor CTO if you don't know who corv is we're the AI hyperscaler we bring the latest Technologies to AI Enterprises all over the world faster and more reliable than anyone else in the last decade we have seen an explosion of workloads running on kubernetes from e-commerce platforms to gaming sers web application and databases now it's the AI era at Cove we decided to take advantage of kubernetes superpowers to run our customers training and inference workloads when you think about running a training job on thousands of nodes or scaling up and down your inference platform based on demand it all makes sense but what makes it a harder problem than usual well you know gpus are scarce and expensive you also want to use the latest and greatest Tech as soon as it's available the definition of good has evolved it's not only reliability and availability like before we are also talking about performance and how long it takes to train a new model and we want to solve for all of that as quickly as possible without interrupting researchers and developers so I hope you agree with with me that solving heart problems is the fun part and let's dive in as you can see there are ton of complex physical components that have direct impact to your hyperconnected training cluster in kubernetes any change in any layer of the stack can impact the cluster health or the job performance and if something goes wrong even as little as a network cable bent to sharply it has detrimental impact to the entire cluster silent data corruption might also occur and can severely affect model quality and repeat offenders and intermittent failur are not in nosense they are the obstacle for experimenting and getting things done quickly as a platform team I need to maintain a healthy resilient and performant AI training clusters so how can I do it on kubernetes well it is possible possible but it's not as easy and that's something that everyone in the industry is now grappling with so how big of a challenge this big this stats were published by meta this summer in their Lama three her of models paper and it describes the interruptions experience of a 54 day pre-training period as you can see they experience 466 total job interruptions out of them 417 of them were unexpected interruptions and 78 of those were H related to suspected hardw failures unfortunately for many teams you might not even have these insigh
