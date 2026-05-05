---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Kevin Klues", "Yuan Chen", "NVIDIA"]
sched_url: https://kccncna2024.sched.com/event/1i7ol/which-gpu-sharing-strategy-is-right-for-you-a-comprehensive-benchmark-study-using-dra-kevin-klues-yuan-chen-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Which+GPU+Sharing+Strategy+Is+Right+for+You%3F+A+Comprehensive+Benchmark+Study+Using+DRA+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Which GPU Sharing Strategy Is Right for You? A Comprehensive Benchmark Study Using DRA - Kevin Klues & Yuan Chen, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Kevin Klues, Yuan Chen, NVIDIA
- Schedule: https://kccncna2024.sched.com/event/1i7ol/which-gpu-sharing-strategy-is-right-for-you-a-comprehensive-benchmark-study-using-dra-kevin-klues-yuan-chen-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Which+GPU+Sharing+Strategy+Is+Right+for+You%3F+A+Comprehensive+Benchmark+Study+Using+DRA+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Which GPU Sharing Strategy Is Right for You? A Comprehensive Benchmark Study Using DRA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ol/which-gpu-sharing-strategy-is-right-for-you-a-comprehensive-benchmark-study-using-dra-kevin-klues-yuan-chen-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Which+GPU+Sharing+Strategy+Is+Right+for+You%3F+A+Comprehensive+Benchmark+Study+Using+DRA+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nOgxv_R13Dg
- YouTube title: Which GPU Sharing Strategy Is Right for You? A Comprehensive Benchmark Study Us... K. Klues, Y. Chen
- Match score: 0.968
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/which-gpu-sharing-strategy-is-right-for-you-a-comprehensive-benchmark/nOgxv_R13Dg.txt
- Transcript chars: 33672
- Keywords: gpu, resource, sharing, slicing, limits, performance, partitioning, inference, workload, memory, access, device, strategy, isolation, request, resources, without, server

### Resumo baseado na transcript

my name is Kevin Clues this is my colleague Yuan Chen uh we're going to be talking today about which GPU sharing strategy is right for you uh with a comprehens comprehensive Benchmark study using Dr um so you know to kick things off why do we even care about uh sharing gpus um well at the end of the day it's really about increasing the utilization of the gpus that you have uh access to as well as decreasing the costs because the more efficient use of the gpus

### Excerpt da transcript

my name is Kevin Clues this is my colleague Yuan Chen uh we're going to be talking today about which GPU sharing strategy is right for you uh with a comprehens comprehensive Benchmark study using Dr um so you know to kick things off why do we even care about uh sharing gpus um well at the end of the day it's really about increasing the utilization of the gpus that you have uh access to as well as decreasing the costs because the more efficient use of the gpus that you have the fewer gpus that you need to get your work done and that then obviously leads to uh lower costs um this has been a Hot Topic uh at lots of the past previous cucon over the years um cucon Paris uh just last April uh there was five talks that were related to GPU sharing in Chicago there was a couple um and then every cucon all the way back through 2019 there's been some talk that had to do with how can I make more efficient use of my gpus using some type of GPU sharing strategy um a couple of use cases for for GPU sharing uh that are that are uh the most obvious ones um or if you have a single user that wants to run multiple applications on top of some GPU uh if he's trying to do you know multiple inference jobs uh for for testing um uh what the type of applications that he's trying to run um you can also have a single tenant with multiple users so a couple of different users that want to share access to a GPU because they're running jupyter notebooks they're trying to um you know build uh models that they want to do for training but they don't have all the details worked out and so they just want to use a subset of a GPU to test things out before they run their their full training job over potentially you know multiple gpus um and there's also use cases for things uh that are more multi-tenant where you want to have multiple users running apps on top of a single GPU in some kind of environment where uh that's appropriate for manage cloud services uh that need to be multi-tenant um there's two primary methodologies for for for doing uh GPU sharing sharing in general uh and that's Space versus time partitioning um where space partitioning uh has the advantage that if you have two workloads uh that you're trying to run um on top of a single GPU um both of those workloads will be fully resident at all times because they share access to the GPU in space rather than time there's no Contex switching overhead because they're always there and you get predictable performance from from these two
