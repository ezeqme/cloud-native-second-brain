---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Data Processing + Storage"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Lu Qiu", "Chanchan Mao", "LanceDB"]
sched_url: https://kccncna2025.sched.com/event/27FXF/highly-scalable-ai-search-engine-and-ai-data-lake-with-kubernetes-and-lancedb-lu-qiu-chanchan-mao-lancedb
youtube_search_url: https://www.youtube.com/results?search_query=Highly+Scalable+AI+Search+Engine+and+AI+Data+Lake+With+Kubernetes+and+LanceDB+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Highly Scalable AI Search Engine and AI Data Lake With Kubernetes and LanceDB - Lu Qiu & Chanchan Mao, LanceDB

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Lu Qiu, Chanchan Mao, LanceDB
- Schedule: https://kccncna2025.sched.com/event/27FXF/highly-scalable-ai-search-engine-and-ai-data-lake-with-kubernetes-and-lancedb-lu-qiu-chanchan-mao-lancedb
- Busca YouTube: https://www.youtube.com/results?search_query=Highly+Scalable+AI+Search+Engine+and+AI+Data+Lake+With+Kubernetes+and+LanceDB+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Highly Scalable AI Search Engine and AI Data Lake With Kubernetes and LanceDB.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXF/highly-scalable-ai-search-engine-and-ai-data-lake-with-kubernetes-and-lancedb-lu-qiu-chanchan-mao-lancedb
- YouTube search: https://www.youtube.com/results?search_query=Highly+Scalable+AI+Search+Engine+and+AI+Data+Lake+With+Kubernetes+and+LanceDB+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ILolPtZGSXU
- YouTube title: Highly Scalable AI Search Engine and AI Data Lake With Kubernetes and Lance... Lu Qiu & Chanchan Mao
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/highly-scalable-ai-search-engine-and-ai-data-lake-with-kubernetes-and/ILolPtZGSXU.txt
- Transcript chars: 28663
- Keywords: search, format, actually, already, basically, storage, create, column, together, information, version, models, multimodal, operation, source, columns, metadata, better

### Resumo baseado na transcript

I know it's really late and we want to go eat dinner and stuff, but we'll make it quick, I promise. Um, we have a great talk prepared for you guys today on how we built a highly scalable AI search engine and AI data lakeink with Kubernetes and Lance DB. So, with all of these three V's together, it's pretty clear that traditional data infrastructure meant for tabular data is not really designed for teams trying to build the next generation of AI applications, infrastructure, or models. You're also paying for extra infrastructure costs for these multiple systems and copying data back and forth. So naturally, the next question to ask is, is there a system that makes storing and working with AI data much easier, that's less costly, and can improve engineer productivity? And you also have the ability to run multiple workloads with compute storage separation in the same system.

### Excerpt da transcript

Okay, we're gonna get started. Um, thank you guys for all being here. I know it's really late and we want to go eat dinner and stuff, but we'll make it quick, I promise. Um, we have a great talk prepared for you guys today on how we built a highly scalable AI search engine and AI data lakeink with Kubernetes and Lance DB. Um, I'm Chan. I'm Deil at Lance DB and I'm here with Lou, who is a data engineer at Lance DB as well. Okay, so before we get into how we built this, let's kind of start with why. So today, everybody is interested in AI. Everybody has the same access to the same models, to the same advanced techniques. So when you're building an AI feature for your company, what really differentiates your AI features from your competitor's AI features? And the answer to that is data. specifically your data and how you connect your enterprise data to your AI features and agents. And that's what really sets apart a commodity from a differentiated AI product. And so there's three ways to think about data.

There's volume, velocity, and variety. These are the three V's of data which are very different today because of AI. So first is volume. The amount of data that you're dealing with. AI data is just so much larger. Tabular data is pretty small. Each row is about, you know, 150 bytes. You add on OpenAI embeddings, which is already an order of magnitude larger. Then you start adding images and videos. Now we're at several order orders of magnitudes larger than what we started with. And this is still all in one single row. So somehow we went from about 145 bit bytes per row to now almost 50 megabytes. So that was volume. Now we are at variety velocity. Sorry, that should be velocity. Uh, velocity is the speed at which data is being generated. Velocity is much higher now because of AI. We're no longer generating data based on human input or manual input. We're generating that data automatically via models at hundreds or even thousands of tokens per second. So now, not only is data larger, they're also being created much faster than before.

And lastly is variety, which is the kinds of data that we're dealing with. AI applications and AI models are often multimodal. It's not about numbers, dates, and strings anymore. There's also prompts, long- form text, images, videos, and embeddings. So, with all of these three V's together, it's pretty clear that traditional data infrastructure meant for tabular data is not really designed for teams trying to build the next g
