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
speakers: ["John Belamaric", "Google", "Patrick Ohly", "Intel"]
sched_url: https://kccncna2024.sched.com/event/1i7pv/better-together-gpu-tpu-and-nic-topological-alignment-with-dra-john-belamaric-google-patrick-ohly-intel
youtube_search_url: https://www.youtube.com/results?search_query=Better+Together%21+GPU%2C+TPU+and+NIC+Topological+Alignment+with+DRA+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Better Together! GPU, TPU and NIC Topological Alignment with DRA - John Belamaric, Google & Patrick Ohly, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: John Belamaric, Google, Patrick Ohly, Intel
- Schedule: https://kccncna2024.sched.com/event/1i7pv/better-together-gpu-tpu-and-nic-topological-alignment-with-dra-john-belamaric-google-patrick-ohly-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Better+Together%21+GPU%2C+TPU+and+NIC+Topological+Alignment+with+DRA+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Better Together! GPU, TPU and NIC Topological Alignment with DRA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pv/better-together-gpu-tpu-and-nic-topological-alignment-with-dra-john-belamaric-google-patrick-ohly-intel
- YouTube search: https://www.youtube.com/results?search_query=Better+Together%21+GPU%2C+TPU+and+NIC+Topological+Alignment+with+DRA+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9CiEw1K0SwM
- YouTube title: Better Together! GPU, TPU and NIC Topological Alignment with DRA - John Belamaric & Patrick Ohly
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/better-together-gpu-tpu-and-nic-topological-alignment-with-dra/9CiEw1K0SwM.txt
- Transcript chars: 31198
- Keywords: gpu, driver, resource, device, available, actually, attributes, constraints, devices, request, certain, nvidia, workload, patrick, another, better, scheduling, little

### Resumo baseado na transcript

okay good morning everyone I hope you had an entertaining and informative Cube con so far and we certainly hope to continue along those lines with our talk today about Better Together topological alignment with Dr um my name is Patrick oie I am a principal engineer at Intel working on kubernetes and Cloud native Technologies among various maintainer roles in in kubernetes my main activity and main focus has been on Dynamic resource allocation for the last 3 years and I'm John B from Google um so I'm been

### Excerpt da transcript

okay good morning everyone I hope you had an entertaining and informative Cube con so far and we certainly hope to continue along those lines with our talk today about Better Together topological alignment with Dr um my name is Patrick oie I am a principal engineer at Intel working on kubernetes and Cloud native Technologies among various maintainer roles in in kubernetes my main activity and main focus has been on Dynamic resource allocation for the last 3 years and I'm John B from Google um so I'm been involved in open source kubernetes for many years now um and Patrick and I are two of the co-chairs of the device management working group which has sort of Taken uh adopted what Patrick started with Dr and uh pushing it through to the Finish Line um uh as our third co-chair is here in the front row so um go ahead yeah in this talk I'll cover the basics what a Dr is because I'm not assuming that everyone is so familiar with it as we are um and I will give you the latest news about where we are and then John will continue talking about the advanced topics about how we envision top topological alignment to be done with Dr going forward so Dynamic resource allocation as I said it has been ongoing for a while you may have heard about it and it was Alpha in previous kubernetes uh releases we find finally figured out which part we actually can and want to promote towards beta and GA around the time frame of kubernetes 131 that's where we did a major overhaul of the entire API so it was a breaking change in 131 but it set us on a path to where we are now where that same API is almost unmodified as beta in 132 that is a big milestone because now we are sure that this API will be around for at least three releases a bit longer depending on how long we want to keep it unchanged it's available um we are doing Buck fixes for it so I highly recommend that if you have been waiting now is the time to get engaged and ask your vors about a Dr driver ask your Cloud providers whether they can enable Dr for you because it's off by default still it is a an API Group and there are rules in cators that say that those need to be off yeah I I'll interject there that for GK uh we will we do plan to make um Dr available as an optional you can enable um with the with the release of 132 in in a rapid Channel yeah so that sets us on a path towards GA we don't have a exact timeline yet it now entirely depends on your feedback on whatever we find out but we are still need to change perha
