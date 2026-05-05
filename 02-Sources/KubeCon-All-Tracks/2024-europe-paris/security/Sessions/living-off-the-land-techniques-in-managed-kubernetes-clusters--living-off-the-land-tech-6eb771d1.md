---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Ronen Shustin", "Shay Berkovich", "Wiz"]
sched_url: https://kccnceu2024.sched.com/event/1YeRm/living-off-the-land-techniques-in-managed-kubernetes-clusters-ronen-shustin-shay-berkovich-wiz
youtube_search_url: https://www.youtube.com/results?search_query=Living+off+the+Land+Techniques+in+Managed+Kubernetes+Clusters+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Living off the Land Techniques in Managed Kubernetes Clusters - Ronen Shustin & Shay Berkovich, Wiz

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Ronen Shustin, Shay Berkovich, Wiz
- Schedule: https://kccnceu2024.sched.com/event/1YeRm/living-off-the-land-techniques-in-managed-kubernetes-clusters-ronen-shustin-shay-berkovich-wiz
- Busca YouTube: https://www.youtube.com/results?search_query=Living+off+the+Land+Techniques+in+Managed+Kubernetes+Clusters+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Living off the Land Techniques in Managed Kubernetes Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRm/living-off-the-land-techniques-in-managed-kubernetes-clusters-ronen-shustin-shay-berkovich-wiz
- YouTube search: https://www.youtube.com/results?search_query=Living+off+the+Land+Techniques+in+Managed+Kubernetes+Clusters+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aAxl90o910g
- YouTube title: Living off the Land Techniques in Managed Kubernetes Clusters - Ronen Shustin & Shay Berkovich
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/living-off-the-land-techniques-in-managed-kubernetes-clusters/aAxl90o910g.txt
- Transcript chars: 26794
- Keywords: cluster, access, config, techniques, perform, fluent, basically, clusters, identity, course, python, network, attacker, server, living, definition, attack, worker

### Resumo baseado na transcript

hello everybody bonjour um thanks for sticking around Welcome to our session living of the land techniques in manage kubernetes clusters my name is Shay sha bovitz I'm proud to be a part of amazing wi threat research team you might know us from these projects and with me today and I'm Rustin I'm from The Whiz vulnerability research team and you might know us from cool researches like broken Sesame uh bing bang uh and many more all right so what are we talking here today living of the

### Excerpt da transcript

hello everybody bonjour um thanks for sticking around Welcome to our session living of the land techniques in manage kubernetes clusters my name is Shay sha bovitz I'm proud to be a part of amazing wi threat research team you might know us from these projects and with me today and I'm Rustin I'm from The Whiz vulnerability research team and you might know us from cool researches like broken Sesame uh bing bang uh and many more all right so what are we talking here today living of the land techniques let's go to Basics let's start with the definition Miriam Webster D dictionary defines living of the land as getting food by farming hunting Etc okay we know that but there is this element of using what's available in the environment and that's so true for classic cyber security definition right Al Bet in a classic definition it's talking more about binaries binaries on the host right so the that those two big projects GT GT4 beans lbas projects that pretty much a list categorized list and collection of the binaries that can be exploited by the attackers once they have the initial access on the host okay so my favorite from the ocp days for those in the know uh was the CER which I used to download enumeration scripts from on to my Windows host um in the the absence of curl or W get for example that's classic example and that's fine that was okay back then when when we said initial access and attacker we thought about VM or host perhaps after escaping some kind of application web application right finding the RC however this has changed right now attacker might find themselves in different context it can be pod within the kubernetes of course it can be node it can perhaps even be lum function right they might own the Lambda function in the cloud okay so as the definition of attack chain and the attack processes has evolved so should the definition of living of the land techniques evolve just like the Metapod Pokemon okay so for the definition for the updated definition I want to take you to the cisa join guidance um so they released it in February 10th if I'm not mistaken so pretty much uh a month ago uh cisa and all lighted agencies released the guidance for on pram and Cloud living of the L techniques and even though they released it past our cfp submission and acceptance we thought it's going to be shame not to include it because uh what they found there their thoughts really resonated with us so let's take their definition native tools and processes on syste
