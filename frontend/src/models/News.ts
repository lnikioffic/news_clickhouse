import NewsBase from "./NewsBase"

export default interface News extends NewsBase {
    uuid: string,
    created_at: string,
    updated_at: string
}