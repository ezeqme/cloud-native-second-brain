---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["AI ML", "Platform Engineering", "Runtime Containers", "SRE Reliability"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iWAL/wasmedge-cross-platform-high-performance-lightweight-embeddable-multi-modal-llm-runtime-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=WasmEdge%3A+Cross-Platform%2C+High-Performance%2C+Lightweight%2C+Embeddable+Multi-Modal+LLM+Runtime+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# WasmEdge: Cross-Platform, High-Performance, Lightweight, Embeddable Multi-Modal LLM Runtime | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iWAL/wasmedge-cross-platform-high-performance-lightweight-embeddable-multi-modal-llm-runtime-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=WasmEdge%3A+Cross-Platform%2C+High-Performance%2C+Lightweight%2C+Embeddable+Multi-Modal+LLM+Runtime+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre WasmEdge: Cross-Platform, High-Performance, Lightweight, Embeddable Multi-Modal LLM Runtime | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iWAL/wasmedge-cross-platform-high-performance-lightweight-embeddable-multi-modal-llm-runtime-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=WasmEdge%3A+Cross-Platform%2C+High-Performance%2C+Lightweight%2C+Embeddable+Multi-Modal+LLM+Runtime+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5_wTuySm7lE
- YouTube title: WasmEdge: Cross-Platform, High-Performance, Lightweight, Embeddable Multi-Modal LLM Runtime | PLT
- Match score: 0.976
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/wasmedge-cross-platform-high-performance-lightweight-embeddable-multi/5_wTuySm7lE.txt
- Transcript chars: 6314
- Keywords: language, python, running, application, models, translation, wasm, assembly, instead, applications, important, support, multiple, framework, distributions, newsletter, lightweight, biggest

### Resumo baseado na transcript

so um hello everyone um my name is Michael Yen and I'm the uh Mainer of the wasm edge project so wasm Edge is a web assembly around time at cncf and uh but here um instead of telling give me another talk about what is web assembly I want to talk about one of the biggest use case of web s that we uh that we have seen you know in particular it's in jni you know so um at current times we have Community users using wage to

### Excerpt da transcript

so um hello everyone um my name is Michael Yen and I'm the uh Mainer of the wasm edge project so wasm Edge is a web assembly around time at cncf and uh but here um instead of telling give me another talk about what is web assembly I want to talk about one of the biggest use case of web s that we uh that we have seen you know in particular it's in jni you know so um at current times we have Community users using wage to run large language model and they have over 200,000 machines running was Ed and large language model just think about that and I'll tell you what what problems they solving using this particular software at this moment so the problem we are trying to solve is to run open source jni models including large language models voice to text text to voice text to image video to uh video to language models on your own infrastructure or bundle it with your own applications okay so if this is not of interest to you for all you want is to give your data and give your money to open AI then I think the rest of talk wouldn't be that interesting to you but if this is um but if this is what you want then my next question to most people is that how do you run it right you know if you want to run large language model applications on your own info how do what what text tack do you use and most people's answer is Pyon you know isn't that obvious you know that's the large language model are all training Python and you know they py toor and everything but I want to make a convincing case against python why not python you know I don't want to U be bad Ming about any of the technology I mentioned here but I I think it's important to to mention some of those in order to say why why we are different right so one of the biggest problem with python it's extremely bloated and uh um we and also when you do things like uh encoding um you know decoding it's extremely slow and it's not just me saying that you know if you look at Python's doer image the doer image for py toor is 8 gigb okay 8 gigb of doer image imagine running it on your H devices like our users running in the car and Raspberry Pi orange pie and you know things like that you need eight gigabytes of disk space and memory to run at so python in a lot of use cases python is not a good choice then if if not python you know I think most people are using AMA you know that's I use AMA too running on my own computer however running it on the edge or running it on say uh uh on on a production server I don't feel this
