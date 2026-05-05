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
themes: ["AI ML"]
speakers: ["Shirley Bailes", "Director of Software Ecosystem Strategy", "Intel"]
sched_url: https://kccncna2024.sched.com/event/1iCOy/sponsored-keynote-the-future-of-genai-cloud-native-blueprints-with-opea-shirley-bailes-director-of-software-ecosystem-strategy-intel
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+The+Future+of+GenAI%3A+Cloud+Native+Blueprints+with+OPEA+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Sponsored Keynote: The Future of GenAI: Cloud Native Blueprints with OPEA - Shirley Bailes, Director of Software Ecosystem Strategy, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Shirley Bailes, Director of Software Ecosystem Strategy, Intel
- Schedule: https://kccncna2024.sched.com/event/1iCOy/sponsored-keynote-the-future-of-genai-cloud-native-blueprints-with-opea-shirley-bailes-director-of-software-ecosystem-strategy-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+The+Future+of+GenAI%3A+Cloud+Native+Blueprints+with+OPEA+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: The Future of GenAI: Cloud Native Blueprints with OPEA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iCOy/sponsored-keynote-the-future-of-genai-cloud-native-blueprints-with-opea-shirley-bailes-director-of-software-ecosystem-strategy-intel
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+The+Future+of+GenAI%3A+Cloud+Native+Blueprints+with+OPEA+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ddrTvJFKtus
- YouTube title: Sponsored Keynote: The Future of GenAI: Cloud Native Blueprints with OPEA - Shirley Bailes
- Match score: 0.984
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sponsored-keynote-the-future-of-genai-cloud-native-blueprints-with-ope/ddrTvJFKtus.txt
- Transcript chars: 4696
- Keywords: application, applications, goldie, source, recipes, generative, knowledge, llm, native, microservice, generate, answer, actually, generation, vectors, choose, morning, foundation

### Resumo baseado na transcript

good morning hi cucon I'm Shirley Bales and I lead software open ecosystem strategy at Intel and I'm here today to talk to you about an open source project that Intel contributed to the Linux Foundation Ai and data Community it's called open platform for Enterprise AI or Opa it's Opia Opia is an industrywide effort and you can see a number of Partners on the screen here it provides microservice recipes for building Cloud native generative AI applications helping you simplify the development production and Adoption of generative AI

### Excerpt da transcript

good morning hi cucon I'm Shirley Bales and I lead software open ecosystem strategy at Intel and I'm here today to talk to you about an open source project that Intel contributed to the Linux Foundation Ai and data Community it's called open platform for Enterprise AI or Opa it's Opia Opia is an industrywide effort and you can see a number of Partners on the screen here it provides microservice recipes for building Cloud native generative AI applications helping you simplify the development production and Adoption of generative AI in the Enterprise we're going to walk through an example application with the help of a couple of friends so you might recognize these lovable characters fippy and Goldie and they love attending cncf events they want to know what's all the fun things that are going on at cubon in Salt Lake City this week they're pretty techsavvy and they want to use AI to generate an answer now as cucon is well underway there's no time no time to actually train a model on the event schedule so and that would really just be way too expensive so we're going to need to use retrieval argumented generation also known as rag to inject some fresh knowledge into a large language model called an llm let's see how it works to create a chat plus Q&A rag application we first need a knowledge base somewhere to begin with and in this case we're going to use a conference schedule we're going to feed the text from the conference site into the app to serve as our knowledge base we then extract the copy we'll break it into phras into phrases and then extract the phrases into vectors the vectors will then populate a vector database and what you see here is a knowledge base for the rag when fippi actually ask Goldie what are some fun things that we can do at cucon this week the application then transforms the question into these vectors A retriever then searches the database for the related data and the question in context are then injected into the llm IT augments the answer generation the model then generates an answer for fippi and Goldie so've got rag again let's retrieve augment and generate so here are the some events that kicked off the week and props to those of you who went to the house of cube last night and also made it to the run at 7: a.m.

this morning if you set out to build a chat service with rag like this you're probably going to be overwhelmed there's dozens of vector databases out there um redis milis chroma and you would need to choose between a
