export function getDateString(dateStr: string): string {
    const date = new Date(dateStr)
    const day = date?.getDay() ?? '00'
    const month = date?.getMonth() ?? '00'
    const year = date?.getFullYear() ?? '0000'

    return `${day}.${month}.${year}`
}