---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Serverless"
themes: ["Storage Data"]
speakers: ["Yuval Lifshitz", "Huamin Chen", "Red Hat"]
sched_url: https://kccncna2021.sched.com/event/lV3P/real-time-data-anonymization-the-serverless-way-yuval-lifshitz-huamin-chen-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Real-Time+Data+Anonymization+the+Serverless+Way+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Real-Time Data Anonymization the Serverless Way - Yuval Lifshitz & Huamin Chen, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Serverless]]
- Temas: [[Storage Data]]
- País/cidade: United States / Los Angeles
- Speakers: Yuval Lifshitz, Huamin Chen, Red Hat
- Schedule: https://kccncna2021.sched.com/event/lV3P/real-time-data-anonymization-the-serverless-way-yuval-lifshitz-huamin-chen-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Real-Time+Data+Anonymization+the+Serverless+Way+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Real-Time Data Anonymization the Serverless Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3P/real-time-data-anonymization-the-serverless-way-yuval-lifshitz-huamin-chen-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Real-Time+Data+Anonymization+the+Serverless+Way+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1E5Q-ErF2sI
- YouTube title: Real-Time Data Anonymization the Serverless Way - Yuval Lifshitz & Huamin Chen, Red Hat
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/real-time-data-anonymization-the-serverless-way/1E5Q-ErF2sI.txt
- Transcript chars: 20749
- Keywords: bucket, notification, serverless, solution, storage, message, notifications, object, function, information, functions, define, events, privacy, personal, another, endpoint, multiple

### Resumo baseado na transcript

In this talk, we will walk you through our serverless architecture to anonymize personal sensitive data to preserve data privacy. First, let's look at the global legislation landscapes on data protection and privacy preservation. In fact, in many use cases, especially machine learning, the privacy of the private personal privacy privacy information are not used at all. And the rest of the presentation, our use case is to anonymize uh data that is in hosted uh storage environment. So, KEDA or Kubernetes event-driven uh architecture is a lightweight and uh service provider oriented. So, the KEDA serverless functions use the machine learning algorithms to detect objects of mostly personal and sensitive information in within the image.

### Excerpt da transcript

Welcome to our CubeCon North America 2021 presentation. It is our pleasure to meet you virtually in this event. In this talk, we will walk you through our serverless architecture to anonymize personal sensitive data to preserve data privacy. Here is the agenda for today. First, let's look at the global legislation landscapes on data protection and privacy preservation. What's their impacts on our industry and how should we address to these challenges? Next, we present to you the solution architecture to our target use case, that is to anonymize personal and sensitive data from images that are in a hosted storage environment. The rest of the talk will deep dive into each of the building blocks. We will show to you how we use adapt and fine-tune these technologies to meet our scalability and security goals. Data protection and privacy is an increasingly important issue for global data controllers. Care must be taken to process, exchange, or store sensitive personal identifiable information and honor privacy provinces.

So, here we have a diagram from the United Nations uh dated year 2020. About 66% of the countries in the world have data protection laws. For reference, just like half of year before that, the number is about 50%. So, we anticipate more and more countries in the world will have data protection laws in the future. The IT industry addressed to such requirements by using two techniques, pseudonymization and anonymization. The difference is whether the transformed data can be traced back to their original forms through another process. For example, data encryption and decryption is a form of pseudonymization. Once encrypted, the data can be used in computation, um transmission, and persistence. In fact, data protection laws such as GDPR recommends uh pseudonymization because it protects data privacy. But, data encryption and decryption often incurs computational and operational or sometimes even financial overhead. So, this is not a solution for all use cases. In fact, in many use cases, especially machine learning, the privacy of the private personal privacy privacy information are not used at all.

So, they can be completely removed from the original data form. And this is the process called data anonymization. According to EU uh GDPR recital 26, data anonymization does not fall into the scope of the law. And the rest of the presentation, our use case is to anonymize uh data that is in hosted uh storage environment. Here is the high-level overvi
